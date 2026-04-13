import psycopg2


def create_tables():
    # Danh sách các câu lệnh SQL để tạo bảng
    commands = (
        """
        CREATE TABLE vendors
        (
            vendor_id   SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE parts
        (
            part_id   SERIAL PRIMARY KEY,
            part_name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE part_drawings
        (
            part_id        INTEGER PRIMARY KEY,
            file_extension VARCHAR(5) NOT NULL,
            draw_data      BYTEA      NOT NULL,
            FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts
        (
            vendor_id INTEGER NOT NULL,
            part_id   INTEGER NOT NULL,
            PRIMARY KEY (vendor_id, part_id),
            FOREIGN KEY (vendor_id)
                REFERENCES vendors (vendor_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )

    conn = None
    try:

        conn = psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="Fptureset@2003"
        )
        cur = conn.cursor()


        for command in commands:
            print(f"Đang thực thi lệnh: {command[:30]}...")
            cur.execute(command)


        cur.close()


        conn.commit()
        print("Netflix! Toàn bộ bảng đã được tạo thành công.")

    except (Exception, psycopg2.DatabaseError) as error:

        print(f"Lỗi rồi nigga: {error}")
    finally:

        if conn is not None:
            conn.close()
            print("Đã đóng kết nối an toàn.")


if __name__ == '__main__':
    create_tables()