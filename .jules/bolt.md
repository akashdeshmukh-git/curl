<!-- SPDX-FileCopyrightText: 2024 curl Project -->
<!-- SPDX-License-Identifier: curl -->

## 2024-05-14 - Optimize AWS SigV4 `uri_encode_path`
**Learning:** `uri_encode_path` encodes one character at a time using `curlx_dyn_addn(new_path, &c, 1)` or `curlx_dyn_addf(new_path, "%%%02X", c)`. We can batch `curlx_dyn_addn` for consecutive unreserved characters.
**Action:** Replace `is_reserved_char(c)` with the equivalent macro `ISUNRESERVED(c)` and add an inner loop to accumulate streaks of unreserved/slash characters, adding them to the dynamic string buffer in one operation instead of character-by-character.
