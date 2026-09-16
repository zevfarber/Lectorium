#!/bin/bash
# finetune.sh — retrain calc.traineddata from every verified page so far.
# Input: a directory of line images + ground truth, one pair per body line:
#     lines/pNNN_LL.png   (the _ocr crop nights_ocr.py makes: flattened, 1x, padded)
#     lines/pNNN_LL.gt.txt (the verified transcription of that line, bare rasm, logical order)
# The pilot's 52 verified lines (nights-frame-01-source.json) are the seed; every page the
# correction+check passes sign off adds 23 more. Retrain when ~100 new lines have accumulated.
#
# Two things that are not obvious and cost a morning to find:
#   * the WordStr box text must be written in REVERSED (visual) character order for Arabic,
#     or training diverges (BCER climbs to 90 %);
#   * the fine-tuned model must be run with --psm 13 (raw line). Under --psm 7 it is no
#     better than the base model, because psm 7 re-normalises the line differently from training.
set -e
[ -d lines ] || unzip -o lines.zip                       # training lines ship zipped
TD=${TD:-td}                     # tessdata dir holding arabest.traineddata (tessdata_best ara)
ITER=${ITER:-1200}
python3 - <<'EOF'
from PIL import Image; import glob
for g in glob.glob('lines/*.gt.txt'):
    b=g[:-7]; w,h=Image.open(b+'.png').size
    t=open(g,encoding='utf-8').read().strip()[::-1]
    open(b+'.box','w',encoding='utf-8').write(f"WordStr 0 0 {w} {h} 0 #{t}\n\t 0 0 {w} {h} 0\n")
EOF
mkdir -p $TD/configs
printf 'tessedit_train_line_recognizer 1\ntextord_fast_pitch_test 1\ntessedit_zero_rejection 1\ntessedit_minimal_rejection 1\ntextord_no_rejects 1\n' > $TD/configs/lstm.train
for b in lines/*.png; do b=${b%.png}; tesseract $b.png $b --psm 7 --tessdata-dir $TD -l arabest lstm.train >/dev/null 2>&1; done
ls lines/*.lstmf > all.lst
combine_tessdata -e $TD/arabest.traineddata arabest.lstm
mkdir -p ck
lstmtraining --model_output ck/calc --continue_from arabest.lstm --traineddata $TD/arabest.traineddata \
  --train_listfile all.lst --max_iterations $ITER --learning_rate 0.0005 2>&1 | grep -E "^At iteration" | tail -3
lstmtraining --stop_training --continue_from ck/calc_checkpoint --traineddata $TD/arabest.traineddata --model_output $TD/calc.traineddata
echo "wrote $TD/calc.traineddata"
