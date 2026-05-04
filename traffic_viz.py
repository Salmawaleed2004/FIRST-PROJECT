import pydeck as pdk
import pandas as pd

# 1. قراءة ملف الـ CSV الخاص بكِ
# تأكدي أن الاسم هنا يطابق تماماً اسم الملف الذي رفعتِهِ
data = pd.read_csv('traffic_data_20260502_162938 (2).csv')

# 2. إعداد طبقة المسارات (TripsLayer) لعمل محاكاة الحركة
layer = pdk.Layer(
    "TripsLayer",
    data,
    get_path="path",          # الإحداثيات
    get_timestamps="timestamps", # الوقت
    get_color=[255, 0, 128],  # لون وردي مثل الصورة التي أعجبتك
    opacity=0.8,
    width_min_pixels=5,
    rounded=True,
    trail_length=600,
    current_time=500,
)

# 3. إعداد مكان الكاميرا فوق الخريطة
view_state = pdk.ViewState(latitude=30.0444, longitude=31.2357, zoom=11, pitch=45)

# 4. دمج الطبقات وعرض الخريطة النهائية
r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/dark-v10')
r.to_html("traffic_simulation_result.html")
