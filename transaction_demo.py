import psycopg2


def add_part_and_vendor(part_name, vendor_name):

    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="Fptureset@2003")
        cur = conn.cursor()

        # 1. Thêm nhà cung cấp mới
        cur.execute("INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING vendor_id", (vendor_name,))
        vendor_id = cur.fetchone()[0]

        # 2. Thêm linh kiện mới
        cur.execute("INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id", (part_name,))
        part_id = cur.fetchone()[0]

        # 3. Liên kết chúng lại trong bảng trung gian vendor_parts
        cur.execute("INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s)", (vendor_id, part_id))

        # CHỐT HẠ: Nếu đến đây không có lỗi, lưu tất cả!
        conn.commit()
        print("Giao dịch thành công! Đã thêm cả 3 bảng.")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        # CÓ LỖI: Hủy bỏ toàn bộ những gì vừa làm ở trên
        if conn:
            conn.rollback()
        print(f"Giao dịch thất bại, đã Rollback! Lỗi: {error}")
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    # Thử thêm linh kiện 'Màn hình' của nhà cung cấp 'Samsung'
    add_part_and_vendor("Màn hình OLED", "Samsung Display")