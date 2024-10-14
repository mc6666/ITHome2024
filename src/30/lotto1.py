from scipy import special as sps
import numpy as np

print('總組數：', sps.comb(39, 5))
print('頭獎組數：', sps.comb(5, 5)*sps.comb(34, 0))
print('二獎組數：', sps.comb(5, 4)*sps.comb(34, 1))
print('三獎組數：', sps.comb(5, 3)*sps.comb(34, 2))
print('四獎組數：', sps.comb(5, 2)*sps.comb(34, 3))

# 各獎組數 
prize_count = np.array([sps.comb(5, 5)*sps.comb(34, 0), sps.comb(5, 4)*sps.comb(34, 1), 
                    sps.comb(5, 3)*sps.comb(34, 2), sps.comb(5, 2)*sps.comb(34, 3)])

# 中獎金額 
prize_amount = np.array([8000000, 20000, 300, 50])
            
# 平均中獎金額
print('平均中獎金額：', round(np.sum(prize_count*prize_amount) / sps.comb(39, 5), 2))

