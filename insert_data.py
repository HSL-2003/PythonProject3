import psycopg2


def insert_vendor(vendor_name):
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING vendor_id;"
    vendor_id = None
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="Fptureset@2003")
        cur = conn.cursor()

        # %s là placeholder để chống SQL Injection (rất quan trọng)
        cur.execute(sql, (vendor_name,))

        # Lấy cái ID vừa được tạo tự động
        vendor_id = cur.fetchone()[0]

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return vendor_id


def insert_vendor_list(vendor_list):
    """ Thêm nhiều nhà cung cấp cùng lúc (Bulk Insert) """
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="Fptureset@2003")
        cur = conn.cursor()

        # executemany sẽ chạy vòng lặp insert cực nhanh
        cur.executemany(sql, vendor_list)

        conn.commit()
        cur.close()
        print(f"Đã thêm thành công {len(vendor_list)} nhà cung cấp!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    # 1. Thử insert 1 thằng lẻ
    v_id = insert_vendor("3M Co.")
    print(f"Vừa thêm nhà cung cấp ID: {v_id}")

    # 2. Thử insert một list (Giống như data ông crawl về)
    vendors = [
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ]
    insert_vendor_list(vendors)