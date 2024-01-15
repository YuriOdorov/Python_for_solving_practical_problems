# from prettytable import PrettyTable
#
# mytable = PrettyTable()
# mytable.add_rows(
#     [[i * j for j in range(1, 11)] for i in range(1, 11)])
# html = mytable.get_html_string()
# print(html)


print('''<html>
  <body>
    <table>''')

for i in range(1, 11):
    print('      <tr>')
    for j in range(1, 11):
        print(f'        <td>{i * j}</td>')

    print('      </tr>')

print('''    </table>
  </body>
</html>''')
