def quick_sort(target_arr):

    # 基準値を定義(配列の中央)
    target_len = len(target_arr)
    pivot_idx = int(target_len / 2)
    pivot = target_arr[pivot_idx]

    # 基準値未満の値を格納する配列
    div_arr_below = [] 
    # 基準値より大きい値を格納する配列
    div_arr_more = []
    # 最終的な値を格納する配列(再起処理が進むと基準値=配列の中身になる)
    div_arr_result = []


    # 基準値と比較して各配列に振り分ける
    for item in target_arr:

        if item < pivot:
            div_arr_below.append(item)
        elif pivot < item:
            div_arr_more.append(item)
        else:
           div_arr_result.append(item)

    # 分割できなくなるまで再起処理する
    if div_arr_below:
        div_arr_below = quick_sort(div_arr_below)
    if div_arr_more:
        div_arr_more = quick_sort(div_arr_more)
    
    # 配列を結合して返却する
    return div_arr_below + div_arr_result + div_arr_more

# テスト
target = [94, 32, 60, 41, 9]
result = quick_sort(target)
print(result)