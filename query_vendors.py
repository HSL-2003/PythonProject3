import psycopg2


def get_vendors():
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="Fptureset@2003")
        cur = conn.cursor()

        # 1. Thực thi câu lệnh SELECT
        print("Đang lấy danh sách nhà cung cấp...")
        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_id")

        # 2. Lấy tất cả dữ liệu về bằng fetchall()
        rows = cur.fetchall()

        for row in rows:
            # row[0] là vendor_id, row[1] là vendor_name
            print(f"ID: {row[0]} | Tên: {row[1]}")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_parts_by_vendor(vendor_id):
    """ Tìm linh kiện dựa vào ID nhà cung cấp (Dùng fetchone) """
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="Fptureset@2003")
        cur = conn.cursor()

        # Dùng %s để truyền tham số an toàn
        cur.execute("SELECT vendor_name FROM vendors WHERE vendor_id = %s", (vendor_id,))

        # Chỉ lấy 1 dòng duy nhất
        row = cur.fetchone()

        if row:
            print(f"Nhà cung cấp của ID {vendor_id} là: {row[0]}")
        else:
            print("Không tìm thấy!")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_vendors()
    print("-" * 30)
    get_parts_by_vendor(3)  # Thử tìm thằng ID số 3