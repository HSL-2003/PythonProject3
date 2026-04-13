import os
import psycopg2
from dotenv import load_dotenv

# 1. Load cấu hình từ file .env
load_dotenv()


def get_db_connection():
    """Hàm tạo kết nối dùng chung"""
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        port=os.getenv('DB_PORT')
    )


def rename_part(part_id, new_name):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        print(f"Đang đổi tên linh kiện ID {part_id} thành {new_name}...")

        # Thay vì callproc, mình dùng CALL trực tiếp
        cur.execute("CALL update_part_name(%s, %s)", (part_id, new_name))

        # Đừng quên commit nếu Procedure của ông không có commit bên trong
        conn.commit()

        cur.close()
        print("Đã thực hiện xong!")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Lỗi rồi nigga: {error}")
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    rename_part(1, 'Màn hình OLED Gen 2')