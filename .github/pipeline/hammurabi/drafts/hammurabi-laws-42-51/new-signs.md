# New signs needed — hammurabi-laws-42-51

Not in signs-cuneiform.json; used by key in units.json. Unicode names checked with `unicodedata.lookup`.

| key | Unicode name | char | values / use here |
|---|---|---|---|
| MAR | CUNEIFORM SIGN MAR | 𒈥 | mar — in i-mar-ra-ar (marārum “to hoe”, XIII 28) |
| UZ3 | CUNEIFORM SIGN UZ3 | 𒍚 | uz, us, uṣ — in i-zu-uz-zu (zâzum “to divide”, XIII 57). Harper’s plate shows the goat-sign; Unicode has no plain “UZ”, the OB syllable uz is UZ₃ |
| BURU14 | CUNEIFORM SIGN EN TIMES GAN2 TENU | 𒂙 | BURU₁₄ = ebūrum “harvest” (XIII 68, XIV 33); Harper’s List of Signs no. 19 “ebûru” |

Suggested signs.py calls:
```
python3 ../run3/signs.py add cuneiform MAR 'CUNEIFORM SIGN MAR' '{"name": "mar", "type": "syllabogram", "sound": "mar", "determines": null, "values": ["mar — in i-mar-ra-ar “he shall hoe” (§44)"], "label": "MAR"}'
python3 ../run3/signs.py add cuneiform UZ3 'CUNEIFORM SIGN UZ3' '{"name": "uz, us, uṣ — the goat-sign", "type": "syllabogram", "sound": "uz", "determines": null, "values": ["uz — in i-zu-uz-zu “they shall divide” (§46)"], "label": "UZ₃"}'
python3 ../run3/signs.py add cuneiform BURU14 'CUNEIFORM SIGN EN TIMES GAN2 TENU' '{"name": "harvest (buru₁₄ / ebūrum)", "type": "logogram", "sound": "BURU₁₄", "determines": null, "values": ["BURU₁₄ = ebūrum “harvest”: ina ebūrim “at harvest” (§47, §49); Harper’s sign list: ebûru"], "label": "BURU₁₄"}'
```

## Reviewer (pass 1, 2026-10-12)
All three confirmed on the plates (MAR XIII 28; UZ3 XIII 57; BURU14 XIII 68, XIV 33 = Harper sign-list no. 19 "ebûru") and by `unicodedata.lookup` (U+12225, U+1235A, U+12099). No change.
