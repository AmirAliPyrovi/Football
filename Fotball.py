
import turtle
import random

# تنظیمات صفحه
screen = turtle.Screen()
screen.setup(1000, 720)
screen.title("Football League")
screen.bgcolor("#101827")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")


# نمایش متن در محیط گرافیکی
def show(lines):
    pen.clear()
    y = 300

    for line in lines:
        pen.penup()
        pen.goto(0, y)
        pen.write(
            line,
            align="center",
            font=("Arial", 16, "bold")
        )
        y -= 32

    screen.update()


# دریافت متن از پنجره Turtle
def get_text(message, default):
    result = screen.textinput("Football League", message)

    if result is None or result.strip() == "":
        return default

    return result.strip()


# دریافت عدد
def get_number(message):
    while True:
        result = screen.textinput("Prediction", message)

        if result is None:
            return 0

        try:
            number = int(result)

            if number >= 0:
                return number

        except ValueError:
            pass


# دریافت تیم ها
teamlist = []

for i in range(1, 7):
    show([
        "FOOTBALL LEAGUE",
        "",
        "REGISTER TEAMS",
        "",
        "Team Number: " + str(i)
    ])

    team = get_text(
        "Enter Team " + str(i),
        "Team " + str(i)
    )

    teamlist.append(team)


# دریافت بازیکنان
plalistyer = []

for i in range(1, 6):
    show([
        "FOOTBALL LEAGUE",
        "",
        "REGISTER PLAYERS",
        "",
        "Player Number: " + str(i)
    ])

    player = get_text(
        "Enter Player " + str(i),
        "Player " + str(i)
    )

    plalistyer.append(player)


# امتیاز کل بازیکنان
total_points = {}

for player in plalistyer:
    total_points[player] = 0


# ساخت برنامه مسابقات
teams_schedule = teamlist.copy()
random.shuffle(teams_schedule)

baziha = []

tedad_team = len(teams_schedule)

for week in range(tedad_team - 1):

    week_games = []

    for j in range(tedad_team // 2):

        team1 = teams_schedule[j]
        team2 = teams_schedule[tedad_team - 1 - j]

        week_games.append((team1, team2))

    baziha.append(week_games)

    teams_schedule = (
        [teams_schedule[0]]
        + [teams_schedule[-1]]
        + teams_schedule[1:-1]
    )


# نمایش برنامه مسابقات
for i in range(len(baziha)):

    lines = [
        "FOOTBALL LEAGUE",
        "",
        "WEEK " + str(i + 1),
        ""
    ]

    for team1, team2 in baziha[i]:
        lines.append(team1 + "  VS  " + team2)

    show(lines)

    screen.textinput(
        "Football League",
        "Press OK to continue"
    )


# شروع مسابقات
for week in range(5):

    weekly_points = {}

    for player in plalistyer:
        weekly_points[player] = 0

    # مسابقات هفته
    for match_number, (team1, team2) in enumerate(
        baziha[week], start=1
    ):

        # نتیجه تصادفی بازی
        goal1 = random.randint(0, 5)
        goal2 = random.randint(0, 5)

        difference = abs(goal1 - goal2)

        if goal1 > goal2:
            winner = 1
        elif goal1 < goal2:
            winner = 2
        else:
            winner = 0

        # پیش بینی بازیکنان
        for player in plalistyer:

            show([
                "FOOTBALL LEAGUE",
                "",
                "WEEK " + str(week + 1),
                "MATCH " + str(match_number),
                "",
                team1 + "  VS  " + team2,
                "",
                "PLAYER: " + player,
                "",
                "Enter Your Prediction"
            ])

            w = get_number(
                player + " - Goals for " + team1
            )

            e = get_number(
                player + " - Goals for " + team2
            )

            point = 0

            # امتیاز پیش بینی نتیجه دقیق
            if w == goal1 and e == goal2:
                point += 10
            else:
                point -= 2

            # امتیاز اختلاف گل
            predicted_difference = abs(w - e)

            if predicted_difference == difference:
                point += 7
            else:
                point -= 2

            # پیش بینی برنده
            if w > e:
                predicted_winner = 1
            elif w < e:
                predicted_winner = 2
            else:
                predicted_winner = 0

            if predicted_winner == winner:
                point += 5
            else:
                point -= 2

            # ثبت امتیاز
            weekly_points[player] += point
            total_points[player] += point

            show([
                "FOOTBALL LEAGUE",
                "",
                "PLAYER: " + player,
                "",
                "Prediction: " + str(w) + " - " + str(e),
                "",
                "Points This Match: " + str(point),
                "Weekly Points: " + str(weekly_points[player]),
                "Total Points: " + str(total_points[player])
            ])

            screen.textinput(
                "Football League",
                "Press OK for next player"
            )

        # نمایش نتیجه واقعی مسابقه
        show([
            "FOOTBALL LEAGUE",
            "",
            "WEEK " + str(week + 1),
            "MATCH RESULT",
            "",
            team1,
            str(goal1) + "  -  " + str(goal2),
            team2,
            "",
            "Goal Difference: " + str(difference)
        ])

        screen.textinput(
            "Football League",
            "Press OK for next match"
        )

    # پایان هفته و مشخص کردن نفر اول
    sorted_week = sorted(
        weekly_points.items(),
        key=lambda x: x[1],
        reverse=True
    )

    lines = [
        "FOOTBALL LEAGUE",
        "",
        "WEEK " + str(week + 1) + " RESULTS",
        "",
        "WEEKLY RANKING",
        ""
    ]

    for rank, (player, points) in enumerate(
        sorted_week, start=1
    ):
        lines.append(
            str(rank) + ". " + player + " : " + str(points)
        )

    show(lines)

    screen.textinput(
        "Football League",
        "Press OK for next week"
    )


# جدول نهایی
final_ranking = sorted(
    total_points.items(),
    key=lambda x: x[1],
    reverse=True
)

lines = [
    "FOOTBALL LEAGUE",
    "",
    "FINAL LEADERBOARD",
    "",
    "CHAMPION: " + final_ranking[0][0],
    "",
    "FINAL POINTS",
    ""
]

for rank, (player, points) in enumerate(
    final_ranking, start=1
):

    lines.append(
        str(rank) + ". " + player + " : " + str(points)
    )

lines += [
    "",
    "THANK YOU FOR PLAYING!"
]

show(lines)

turtle.done()
