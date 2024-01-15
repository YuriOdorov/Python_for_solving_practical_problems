# from prettytable import PrettyTable
# mytable = PrettyTable()
# mytable.add_rows(
#     [
#         [1, 2],
#         [3, 4],
#     ]
# )
# html = mytable.get_html_string()
# print(html)
#

a = [[1, 2], [3, 4]]

print('''<html>
  <body>
    <table>''')

for i in range(2):
    print('      <tr>')
    for j in range(2):
        print(f'        <td>{a[i][j]}</td>')

    print('      </tr>')

print('''    </table>
  </body>
</html>''')
