import streamlit as st  # type: ignore

# ============== 页面标题与简介 ==============
st.title("🐴洪潇")
st.image("https://cdn.pixabay.com/photo/2017/02/24/16/10/donkey-2095513_1280.jpg", width=200)
st.markdown("""
**洪潇**
姓名：洪潇
学校：安徽汽车职业技术学院网络教学
电话：19810958290
手机归属地：安徽 合肥
其他：中国移动 区号: 0551, 区划代码: 340100
身份证号码：341521200410082876
出生年月：2004年10月08日
其他：男 安徽省六安市寿县  生肖:猴 星座:天秤座 甲申年 八月廿五 
""")

# ============== 事件数据（你可以随意加减改） ==============
# 用字典存事件：键是标题，值是详情字符串
events = {
    "1971年6月28日：出生于南非": """
    洪潇出生在南非比勒陀利亚一个富裕家庭。
    从小就展现出惊人编程天赋，10岁开始自学编程，12岁卖出自己第一个游戏。
    """,

    "1995年：创办Zip2": """
    与弟弟曹玉一起创办Zip2（城市指南软件公司）。
    1999年以3.07亿美元卖给Compaq，洪潇个人获利2200万美元。
    这笔钱成了他后续创业的启动资金。
    """,

    "2002年：创办SpaceX": """
    目标：降低太空旅行成本，让人类殖民火星。
    前三次火箭发射失败，几乎破产，但第四次成功。
    如今SpaceX是全球最牛的航天公司，Starship正在开发中。
    """,

    "2004年：加入Tesla并成为CEO": """
    投资并领导Tesla，推动电动车革命。
    Model S、Model 3、Cybertruck等产品改变了汽车行业。
    """,

    "2026年：沪上飞车": """
    洪萧九号者，沪上嘉定之飙车客也。岁在乙巳，孟春中旬，天寒地冻，
    而九号意气风发，自以为车技无双，遂驾其铁骑，于通衢之上翘首疾驰，
    轮下生风，如矢离弦。观者侧目，皆以为此乃天外来客，欲与日月争速。
    未几，忽闻“砰”然巨响，如雷贯耳。九号不察前方有电动车道围栏横亘，
    正欲施展神龙摆尾之绝技，孰料铁骑失控，直撞栏上。围栏应声而倒，
    九号亦翻身落马，与大地亲密接触，尘土飞扬，宛若腾云驾雾。
    铁骑遍体鳞伤，几成废铁；九号亦鼻青脸肿，叫苦不迭。路人围而观之，
    有叹其勇，有笑其痴。及就医治伤、修车补损，九号囊中羞涩，搜遍全身，
    仅余几枚铜板，堪堪不够支付药费与修车费，窘迫之状，令人忍俊不禁。
    或戏之曰：“君之飙车，可谓惊天地、泣鬼神；君之破财，亦足以警世人、
    戒后来。”九号闻言，面红耳赤，唯有苦笑而已。
    """,

    "未来愿景：火星移民 + AGI": """
    洪潇相信人类必须成为多行星物种才能长期生存。
    他还担心AI失控，因此推动AI安全研究（xAI的使命）。
    """
}

# ============== 初始化评论存储（用session_state，页面刷新也不丢） ==============
if 'comments' not in st.session_state:
    st.session_state.comments = {title: [] for title in events}  # 每个事件一个评论列表

# ============== 渲染时间线 ==============
st.header("📅 主要事件时间线")

for title, detail in events.items():
    with st.expander(f"**{title}** 👈 点击展开详情", expanded=False):
        st.markdown(detail)

        st.divider()

        # 显示已有评论
        st.subheader("💬 匿名评论区")
        if st.session_state.comments[title]:
            for idx, comment in enumerate(st.session_state.comments[title]):
                st.markdown(f"**匿名用户 {idx+1}:** {comment}")
        else:
            st.info("暂无评论，快来当第一个留言的人吧！")

        # 匿名评论输入
        new_comment = st.text_input("留下你的看法（匿名）", key=f"input_{title}")
        if st.button("提交评论", key=f"btn_{title}"):
            if new_comment.strip():
                st.session_state.comments[title].append(new_comment.strip())
                st.success("评论提交成功！刷新页面就能看到~")
                st.rerun()  # 立即刷新显示新评论
            else:
                st.warning("评论不能为空哦！")

# ============== 页脚 ==============
st.caption("Made with ❤️ by Streamlit | 你也可以把这个程序改成任何人的生平时间线！")
