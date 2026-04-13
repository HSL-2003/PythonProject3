import psycopg2


def update_vendor(vendor_id, vendor_name):
    sql = """ UPDATE vendors
              SET vendor_name = %s
              WHERE vendor_id = %s """
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="Fptureset@2003")
        cur = conn.cursor()

        # 1. Thực thi câu lệnh Update
        cur.execute(sql, (vendor_name, vendor_id))

        # 2. Kiểm tra xem có bao nhiêu dòng đã được sửa
        updated_rows = cur.rowcount

        # 3. CHỐT HẠ: Phải commit thì thay đổi mới có hiệu lực
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    # Giả sử ông muốn đổi tên nhà cung cấp ID số 1 thành "3M Corp"
    rows = update_vendor(5, "3M Corp")
    print(f"Đã cập nhật thành công {rows} dòng!")