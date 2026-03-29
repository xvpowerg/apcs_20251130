import sys

def main():
    input = sys.stdin.readline            # 快速讀取（資料很多時比較穩）

    m_line = input().strip()              # 先讀第一行：有幾支籤
    m = int(m_line)

    # 籤筒（用 set）
    # 好處：我想問「某支籤在不在」→ 直接問籤筒就好，超快
    draws = set()
    for _ in range(m):
        draws.add(input().strip())        # 把每支籤丟進籤筒（重複的會自動合併）

    ans = 0                               # 答案：目前找到幾對聖筊（預設 0）

    # 一支一支籤拿出來檢查
    for s in draws:
        L = len(s)                        # 這支籤的長度

        # 我們要試很多種 U 的長度 l
        # l 最少 1（U 至少要有 1 個字）
        # l 最大只能到 L//2（不然頭尾會重疊，切不出中間）
        for l in range(1, L // 2 + 1):

            # 先看「頭 l 個字」跟「尾 l 個字」是不是一樣
            # 如果不一樣 → 代表這個 l 不是 U → 換下一個 l
            if s[:l] != s[-l:]:
                continue

            # 如果一樣，表示找到一種 U
            # 那中間剩下的就是 mid（也就是 T）
            mid = s[l:-l]

            # 再直接問籤筒：有沒有這支 mid？
            # 有的話：就代表 (s, mid) 這一對合起來一定能切成左右相同 → 算 1 對
            if mid in draws:
                ans += 1

    print(ans)                             # 印出總共有幾對


main()
