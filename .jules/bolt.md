## 2024-05-14 - Optimize AWS SigV4 `uri_encode_path` string encoding
**Learning:** `uri_encode_path` in AWS SigV4 encodes string characters one by one. By finding streaks of characters that do not need escaping (unreserved chars or slashes), we can batch add them with a single `curlx_dyn_addn`.
**Action:** Replace `is_reserved_char(c)` with the equivalent macro `ISUNRESERVED(c)` and add an inner loop to accumulate streaks of unreserved/slash characters, adding them to the dynamic string buffer in one operation instead of character-by-character.
