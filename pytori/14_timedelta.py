from datetime import datetime, timedelta

# 現在の日時を取得
now = datetime.now()

# 1日後の日時を計算
one_day_later = now + timedelta(days=1)
print(one_day_later)