import requests
from datetime import datetime, timedelta
import random

# 配置项
PUSHPLUS_TOKEN = "你的PUSHPLUS_TOKEN"

def generate_moyu_data():
    today = datetime.now()
    week_days = ['日', '一', '二', '三', '四', '五', '六']
    day_of_week = today.weekday()
    week_day_cn = week_days[day_of_week + 1] if day_of_week != 6 else week_days[0]
    
    # 生成动态问候语
    hour = today.hour
    if 5 <= hour < 9:
        greeting, greeting_emoji = "早上好", "🌅"
    elif 9 <= hour < 12:
        greeting, greeting_emoji = "上午好", "☀️"
    elif 12 <= hour < 14:
        greeting, greeting_emoji = "中午好", "🍚"
    elif 14 <= hour < 18:
        greeting, greeting_emoji = "下午好", "🌤️"
    else:
        greeting, greeting_emoji = "晚上好", "🌙"
    
    # 周末判断及文案生成
    if day_of_week >= 5:
        is_weekend = True
        weekend_text = "就是今天"
        weekend_title_top = "今日是周末"
        weekend_title_card = "今日是周末"
        weekend_desc = f"{greeting}{greeting_emoji}，摸鱼人！工作再忙一定不要忘记休息哦！起身去茶水间，去厕所走走，钱是老板的但命是自己的，祝愿摸鱼人愉快的度过每一天..."
    else:
        is_weekend = False
        weekend_days = 4 - day_of_week if day_of_week < 4 else 6 - day_of_week
        weekend_text = f"{weekend_days} 天"
        weekend_title_top = "距离周末"
        weekend_title_card = "摸鱼总经办提醒您"
        weekend_desc = f"{greeting}{greeting_emoji}，摸鱼人！今天也要努力摸鱼哦！合理规划摸鱼时间，工作摸鱼两不误，让老板看不出来的摸鱼才是最高境界～"
    
    # 摸鱼指数计算
    fish_index = random.randint(50, 100)
    if fish_index >= 90:
        fish_level, fish_color = "鱼鲨", "#e53e3e"
    elif fish_index >= 80:
        fish_level, fish_color = "老油条", "#dd6b20"
    elif fish_index >= 70:
        fish_level, fish_color = "熟练工", "#ed8936"
    else:
        fish_level, fish_color = "新手", "#48bb78"
    fish_text = f"{fish_index}% | {fish_level}"
    
    # 星座运势
    zodiac_list = ["摩羯座", "水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", 
                   "巨蟹座", "狮子座", "处女座", "天秤座", "天蝎座", "射手座"]
    zodiac_quotes = ["灵感爆棚，先摸再说", "摸鱼需谨慎，老板在附近", "适合摸鱼，不宜内卷", 
                     "摸鱼效率MAX", "小心摸鱼被抓", "摸鱼不忘干饭"]
    zodiac = zodiac_list[today.month - 1]
    zodiac_text = f"{zodiac}：{random.choice(zodiac_quotes)}"
    
    # 运势文案
    fortune_texts = [
        "今日宜摸鱼，忌认真工作",
        "摸鱼时记得屏蔽老板，财运+1",
        "适合带薪拉屎，摸鱼指数拉满",
        "小心领导突击检查，建议低调摸鱼",
        "摸鱼虽好，可不要贪杯哦"
    ]
    fortune_text = random.choice(fortune_texts)
    
    # 发薪日计算
    next_month_year = today.year + 1 if today.month == 12 else today.year
    next_month = 1 if today.month == 12 else today.month + 1
    last_day = (datetime(today.year, today.month + 1, 1) - timedelta(days=1)) if today.month != 12 else datetime(today.year + 1, 1, 1) - timedelta(days=1)
    current_day = today.day
    
    salary_configs = [("月初", 1), ("10号", 10), ("15号", 15), ("20号", 20), ("25号", 25), ("月底", last_day.day)]
    salary_items = []
    for name, day in salary_configs:
        if current_day <= day:
            diff = day - current_day
        else:
            next_last_day = (datetime(next_month_year, next_month + 1, 1) - timedelta(days=1)) if next_month != 12 else datetime(next_month_year + 1, 1, 1) - timedelta(days=1)
            target_day = next_last_day.day if name == "月底" else day
            diff = (datetime(next_month_year, next_month, target_day) - today).days
        
        if diff == 0:
            salary_items.append(f"{name}：今天发薪！🎉")
        elif diff == 1:
            salary_items.append(f"{name}：明天发！🥳")
        elif diff < 0:
            salary_items.append(f"{name}：已发薪 ✅")
        else:
            salary_items.append(f"{name}：{diff}天")
    
    # 节日倒计时
    festivals = [
        ("元旦", datetime(2026, 1, 1)),
        ("春节", datetime(2026, 2, 10)),
        ("清明", datetime(2026, 4, 4)),
        ("劳动节", datetime(2026, 5, 1)),
        ("端午", datetime(2026, 6, 19)),
        ("中秋", datetime(2026, 9, 17)),
        ("国庆", datetime(2026, 10, 1))
    ]
    festival_items = [f"{name}：{(date - today).days}天" for name, date in festivals]
    
    # 摸鱼时间轴
    timeline = [
        "09:00 伪装上班",
        "10:30 假装思考",
        "11:30 上午摸鱼",
        "14:00 午后犯困",
        "16:00 深度摸鱼",
        "17:30 准备跑路"
    ]
    
    # 摸鱼语录
    quotes = [
        "有人相爱，有人夜里看海，有人七八个闹钟起不来",
        "奥德彪至死都认为他生活过得不好是因为香蕉拉得不够多",
        "想买一件羽绒服，但是999感冒灵才22块钱，于是又穿短裤出门了",
        "太喜欢上班了，低人一等累死累活还赚不到钱的感觉太迷人了",
        "工资就像大姨妈，一个月来一次，一周左右就没了",
        "人之初性本善 不想上班怎么办",
        "如果坐牢有平替，那一定是上班。",
        "刚喝了一杯美式，好苦，跟我的命一样苦。",
        "漫长的岁月 竟没有一天适合上班",
        "没有困难的工作，只有勇敢的打工人",
        "打工只是一场戏，大家因为贫困而相聚",
        "早上多睡了五分钟，电动车都能拧冒烟",
        "一星期 总有那么5天摸鱼上班",
        "葡萄酒开了都要醒五分钟，人醒了却要立刻去上班",
        "加班不是福报 摸鱼才是王道"
    ]
    quote_text = random.choice(quotes)
    
    return {
        "year": today.year,
        "month": today.month,
        "day": today.day,
        "week_day_cn": week_day_cn,
        "weekend_title_top": weekend_title_top,
        "weekend_title_card": weekend_title_card,
        "weekend_text": weekend_text,
        "weekend_desc": weekend_desc,
        "fish_text": fish_text,
        "fish_color": fish_color,
        "zodiac_text": zodiac_text,
        "fortune_text": fortune_text,
        "salary_items": salary_items,
        "festival_items": festival_items,
        "timeline": timeline,
        "quote_text": quote_text
    }

def push_to_pushplus():
    data = generate_moyu_data()
    
    # 拼接HTML内容
    content = f"""
<div style="width:100%;max-width:600px;margin:0 auto;font-family:'Microsoft YaHei', 'PingFang SC', sans-serif;background:#f5f5f5;padding:15px;">
  <div style="background:#2d3748;color:white;border-radius:8px;padding:18px 20px;margin-bottom:15px;display:flex;justify-content:space-between;align-items:center;">
    <div style="text-align:center;padding:0 5px;margin-right:5px;">
      <div style="font-size:11px;opacity:0.8;margin-bottom:3px;">{data['year']}年 {data['month']}月</div>
      <div style="font-size:36px;font-weight:bold;line-height:1;margin:0 0 5px 0;">{data['day']}</div>
      <div style="font-size:12px;opacity:0.8;background:rgba(255,255,255,0.1);padding:2px 8px;border-radius:4px;display:inline-block;">
        星期{data['week_day_cn']}
      </div>
    </div>
    <div style="flex:1;text-align:center;padding:0 5px;min-width:120px;">
      <div style="font-size:24px;font-weight:bold;letter-spacing:1px;margin:0 0 3px 0;">摸鱼日历</div>
      <div style="font-size:11px;opacity:0.8;">jin tian ni mo yu le ma?</div>
    </div>
    <div style="text-align:center;padding:0 5px;margin-left:5px;">
      <div style="font-size:12px;opacity:0.8;margin-bottom:3px;">{data['weekend_title_top']}</div>
      <div style="font-size:18px;font-weight:bold;">{data['weekend_text']}</div>
    </div>
  </div>

  <div style="background:white;border-radius:8px;padding:15px;margin-bottom:15px;display:flex;gap:15px;box-shadow:0 1px 3px rgba(0,0,0,0.05);">
    <div style="flex:3;">
      <div style="font-size:14px;color:#666;margin-bottom:8px;display:flex;align-items:center;">
        <span style="display:inline-block;width:16px;height:16px;background:#4299e1;border-radius:50%;text-align:center;color:white;font-size:10px;line-height:16px;margin-right:5px;">📅</span>
        {data['weekend_title_card']}
      </div>
      <div style="font-size:14px;color:#333;line-height:1.6;margin-bottom:10px;">{data['weekend_desc']}</div>
      <div style="font-size:14px;color:#666;margin-bottom:5px;">{data['fortune_text']}</div>
      <div style="display:flex;align-items:center;margin-top:8px;">
        <span style="font-size:14px;color:#666;margin-right:8px;">摸鱼指数</span>
        <span style="font-size:14px;font-weight:bold;color:{data['fish_color']};">{data['fish_text']}</span>
      </div>
      <div style="font-size:13px;color:#666;margin-top:5px;">
        <span style="display:inline-block;width:14px;height:14px;background:#ffd700;border-radius:50%;text-align:center;color:white;font-size:10px;line-height:14px;margin-right:3px;">⭐</span>
        {data['zodiac_text']}
      </div>
    </div>
    <div style="flex:1;min-width:80px;">
      <div style="background:#f8f8f8;border-radius:6px;padding:8px;text-align:center;">
        <img src="https://xximg1.meitudata.com/wechat-program/693e5bf550fd1bl4gs928f7732.gif" 
             style="width:100%;max-width:80px;height:auto;border-radius:4px;" 
             alt="摸鱼表情包"/>
      </div>
    </div>
  </div>

  <div style="display:flex;gap:15px;margin-bottom:15px;">
    <div style="flex:1;background:white;border-radius:8px;padding:15px;box-shadow:0 1px 3px rgba(0,0,0,0.05);">
      <div style="font-size:15px;font-weight:bold;color:#333;margin-bottom:10px;display:flex;align-items:center;">
        <span style="display:inline-block;width:18px;height:18px;background:#f6ad55;border-radius:50%;text-align:center;color:white;font-size:10px;line-height:18px;margin-right:5px;">⏰</span>
        今日摸鱼时间轴
      </div>
      <div style="font-size:13px;color:#666;line-height:2;">
        {''.join([f'<div>{item}</div>' for item in data['timeline']])}
      </div>
    </div>
    <div style="flex:1;background:white;border-radius:8px;padding:15px;box-shadow:0 1px 3px rgba(0,0,0,0.05);">
      <div style="font-size:15px;font-weight:bold;color:#333;margin-bottom:10px;display:flex;align-items:center;">
        <span style="display:inline-block;width:18px;height:18px;background:#48bb78;border-radius:50%;text-align:center;color:white;font-size:10px;line-height:18px;margin-right:5px;">💰</span>
        发工资倒计时
      </div>
      <div style="font-size:13px;color:#666;line-height:2;">
        {''.join([f'<div>{item}</div>' for item in data['salary_items']])}
      </div>
    </div>
  </div>
  
  <div style="background:white;border-radius:8px;padding:15px;margin-bottom:15px;box-shadow:0 1px 3px rgba(0,0,0,0.05);">
    <div style="font-size:15px;font-weight:bold;color:#333;margin-bottom:10px;display:flex;align-items:center;">
      <span style="display:inline-block;width:18px;height:18px;background:#f56565;border-radius:50%;text-align:center;color:white;font-size:10px;line-height:18px;margin-right:5px;">🎊</span>
      节日倒计时
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:8px;">
      {''.join([f'<div style="background:#f9f9f9;padding:5px 10px;border-radius:4px;font-size:13px;color:#666;">{item}</div>' for item in data['festival_items']])}
    </div>
  </div>
  
  <div style="background:#f8f9fa;border-radius:8px;padding:15px;font-size:14px;color:#666;border-left:3px solid #90cdf4;">
    {data['quote_text']}
  </div>
  
  <div style="text-align:center;margin-top:15px;">
    <p style="font-size:12px;color:#999;margin:0;">
      本页面仅供精神放松使用，对老板无效。<br>
      摸鱼哲学：摸鱼是职场智慧，不是态度问题
    </p>
  </div>
</div>
    """
    
    # 推送请求
    url = "http://www.pushplus.plus/send"
    payload = {
        "token": PUSHPLUS_TOKEN,
        "title": f"🐟 摸鱼日历 | {data['year']}年{data['month']}月{data['day']}日 星期{data['week_day_cn']}",
        "content": content,
        "template": "html",
        "channel": "wechat",
        "webhook": "",
        "callbackUrl": ""
    }
    
    try:
        response = requests.post(url, json=payload, timeout=15)
        response.raise_for_status()
        result = response.json()
        
        if result.get("code") == 200:
            print("✅ 摸鱼日历推送成功！")
            return True
        else:
            print(f"❌ 推送失败：{result.get('msg', '未知错误')}")
            return False
            
    except Exception as e:
        print(f"❌ 推送异常：{str(e)}")
        return False

def main():
    print("🔄 开始生成摸鱼日历...")
    push_to_pushplus()

if __name__ == "__main__":
    main()
