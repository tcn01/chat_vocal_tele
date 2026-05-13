# Telegram English Learning Bot

Bot tự động học tiếng Anh hàng ngày qua Telegram, tích hợp OpenAI GPT-4o-mini và vận hành bằng GitHub Actions.

## 🚀 Hướng dẫn thiết lập

### 1. Lấy Telegram Token
- Chat với [@BotFather](https://t.me/botfather) trên Telegram.
- Dùng lệnh `/newbot` và đặt tên cho bot.
- Copy mã **API Token**.

### 2. Lấy Telegram Chat ID
- Gửi một tin nhắn bất kỳ cho bot vừa tạo.
- Truy cập URL: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
- Tìm ID trong mục `"chat":{"id":123456789...}`. Đây là ID của bạn.

### 3. Lấy OpenAI API Key
- Truy cập [OpenAI Dashboard](https://platform.openai.com/api-keys) và tạo key mới.

### 4. Cấu hình GitHub Secrets
- Vào repository của bạn trên GitHub.
- Chọn **Settings** > **Secrets and variables** > **Actions**.
- Thêm 3 secret sau:
  - `OPENAI_API_KEY`: Mã OpenAI của bạn.
  - `TELEGRAM_TOKEN`: Token từ BotFather.
  - `TELEGRAM_CHAT_ID`: Chat ID của bạn.

### 5. Chạy thử
- Vào tab **Actions** trên GitHub.
- Chọn workflow **Daily English Bot**.
- Bấm **Run workflow** để test ngay lập tức.

## 🛠 Mở rộng sau này
- **Thêm Tool**: Tạo file mới trong `src/tools/` và gọi trong `main.py`.
- **Audio**: Tích hợp OpenAI TTS API để gửi giọng đọc.
- **Quiz**: Thêm logic phản hồi (Requires a persistent server or Webhook).
