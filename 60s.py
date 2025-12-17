import requests
from datetime import datetime

# -------------------------- 核心配置（替换为自己的） --------------------------
PUSHPLUS_TOKEN = "你的PushPlus Token"  # 你的PushPlus Token
API_URL = "https://60s.viki.moe/v2/60s"

# -------------------------- 工具函数 --------------------------
def get_60s_data():
    """获取每日60s新闻数据"""
    try:
        # 青龙面板若访问接口失败，可添加代理（按需启用）
        proxies = {
            "http": None,
            "https": None
        }
        resp = requests.get(API_URL, timeout=20, proxies=proxies)
        resp.raise_for_status()
        data = resp.json()
        
        if data.get("code") != 200:
            raise Exception(f"接口错误: {data.get('message', '未知错误')}")
        return data["data"]
    except Exception as e:
        print(f"❌ 获取60s数据失败: {str(e)}")
        raise

def format_news_content(data):
    """格式化新闻内容为美观的HTML（适配微信推送）"""
    # 拼接带序号的新闻列表
    news_html = ""
    for idx, news in enumerate(data["news"], 1):
        news_html += f"""
        <div style="padding: 8px 0; border-bottom: 1px solid #f0f0f0; font-size: 16px; line-height: 1.6;">
            <span style="display: inline-block; width: 24px; height: 24px; background: #4299e1; 
                        color: white; border-radius: 4px; text-align: center; font-size: 14px; 
                        line-height: 24px; margin-right: 10px;">{idx}</span>
            {news}
        </div>
        """
    
    # 完整HTML内容（大字体、简洁样式）
    content = f"""
<div style="width:100%;max-width:700px;margin:0 auto;font-family:'Microsoft YaHei', sans-serif;">
    <!-- 头部 -->
    <div style="background:#4299e1;color:white;padding:20px;border-radius:8px;margin-bottom:15px;text-align:center;">
        <h1 style="font-size:24px;margin:0;font-weight:bold;">每日60秒新闻速览</h1>
        <div style="font-size:18px;margin-top:8px;opacity:0.9;">
            {data['date']} | {data['day_of_week']} | {data['lunar_date']}
        </div>
    </div>
    
    <!-- 新闻列表 -->
    <div style="background:white;padding:20px;border-radius:8px;margin-bottom:15px;box-shadow:0 1px 3px rgba(0,0,0,0.1);">
        <div style="font-size:18px;font-weight:bold;color:#333;margin-bottom:15px;">📝 今日热点新闻</div>
        {news_html}
    </div>
    
    <!-- 每日微语 -->
    <div style="background:#f6ad55;color:white;padding:20px;border-radius:8px;text-align:center;">
        <div style="font-size:18px;font-weight:bold;margin-bottom:10px;">💬 每日微语</div>
        <div style="font-size:17px;line-height:1.8;font-style:italic;">「{data['tip']}」</div>
    </div>
    
    <!-- 底部 -->
    <div style="text-align:center;margin-top:15px;font-size:14px;color:#999;">
        数据来源：60s.viki.moe | 更新时间：{data['created']}
    </div>
</div>
    """
    return content

def push_to_pushplus(token, title, content):
    """PushPlus推送（核心功能）"""
    if not token:
        print("⚠️ PushPlus Token未配置，跳过推送")
        return
    
    url = "https://www.pushplus.plus/send"
    headers = {"Content-Type": "application/json"}
    payload = {
        "token": token,
        "title": title,
        "content": content,
        "template": "html",
        "channel": "wechat"
    }
    
    try:
        resp = requests.post(url, json=payload, timeout=15)
        resp.raise_for_status()
        result = resp.json()
        
        if result.get("code") == 200:
            print("✅ 新闻推送成功！")
        else:
            print(f"❌ 推送失败: {result.get('msg', '未知错误')}")
    except Exception as e:
        print(f"❌ 推送异常: {str(e)}")

# -------------------------- 主函数 --------------------------
def main():
    try:
        print("🔄 开始获取每日60s新闻...")
        # 1. 获取数据
        data = get_60s_data()
        # 2. 格式化内容
        news_content = format_news_content(data)
        # 3. 推送标题
        push_title = f"📮 每日60秒新闻"
        # 4. 推送执行
        push_to_pushplus(PUSHPLUS_TOKEN, push_title, news_content)
        print("✅ 全部流程执行完成！")
    except Exception as e:
        print(f"❌ 程序执行失败: {str(e)}")
        # 推送错误信息（可选）
        push_to_pushplus(PUSHPLUS_TOKEN, "60s新闻推送失败", f"错误原因：{str(e)}")

if __name__ == "__main__":
    main()
