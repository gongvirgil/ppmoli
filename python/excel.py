#!/usr/bin/env python
# -* - coding: UTF-8 -* -

import xlrd
import xlwt
from xlutils.copy import copy
# print xlrd.__VERSION__
# print xlwt.__VERSION__
# print xlutils.__VERSION__


def open_excel(filename='excel.xls'):
    try:
        data = xlrd.open_workbook(filename)
        return data
    except Exception, e:
        print str(e)


#
def excel_table_by_name(
    filename='excel.xls', colnameindex=0, by_name=u'Sheet1'
):
    data = open_excel(filename)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows
    colnames = table.row_values(colnameindex)
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


#
def excel_table_by_index(filename='excel.xls', colnameindex=0, by_index=0):
    data = open_excel(filename)
    table = data.sheets()[by_index]
    nrows = table.nrows   # 行数
    # ncols = table.ncols   # 列数
    colnames = table.row_values(colnameindex)   # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


# 新建一个Excel表
def create_excel(filename='excel.xls'):
    workbook = xlwt.Workbook(encoding='ascii')
    workbook.add_sheet(u'Sheet1')
    workbook.add_sheet(u'Sheet2')
    workbook.add_sheet(u'Sheet3')
    workbook.save(filename)
    return workbook


#
def excel_write(
    filename='excel.xls', sheet_index=0, row=0, col=0, label=''
):
    workbook = open_excel(filename)
    wb = copy(workbook)
    wbsheet = wb.get_sheet(sheet_index)
    wbsheet.write(row, col, label)
    wb.save(filename)
    return True


#
def main():
    excel = create_excel('excel_2.xls')
    print excel
    excel = open_excel('excel_1.xls')
    print excel
    print excel.sheets()[0]
    excel_write('excel_2.xls', 0, 0, 0, 'AAA')


if __name__ == "__main__":
    main()
