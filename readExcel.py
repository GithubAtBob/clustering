import xlrd
import redis

workbook = xlrd.open_workbook('C:\\Users\\a1258\\Desktop\\新建文件夹\\03 统计图片中的数据.xlsx')
booksheet = workbook.sheet_by_index(0)

row_system = booksheet.row_values(161)[1:16]
row_driver = booksheet.row_values(167)[1:22]

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

for i in range(1,16):
    r.set(i,row_system[i-1])
for i in range(0,21):
    r.set(20+i*5,row_driver[i])