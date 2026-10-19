## 2024-05-13 - [O(1) strlen]
**Learning:** In the curl codebase, `curlx_strlen(x)` is an O(1) macro that directly accesses the `len` property of a custom string struct. Therefore, placing it inside a loop condition `for(i = 0; i < curlx_strlen(str); i++)` is actually perfectly fine and NOT an O(n^2) performance bottleneck like a normal `strlen()` would be!
**Action:** Do not attempt to cache `curlx_strlen` results outside of loops. Focus on real performance bottlenecks, such as proper C-string `strlen()` in loop conditions or inner loops doing unnecessary work.
