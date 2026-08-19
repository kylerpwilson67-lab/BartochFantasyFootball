from espn_api.football import League

# 1. League Details
league_id = 2069239128 
year = 2026           
espn_s2 = 'AEAfPvWR7TbBIWfPa2ndLOLG9UvHm8mP8igll5Jc3ePctEK%2FRnu%2BlDdHbi7xmH10JNNdfjzzNdgyccSQYQUm4Glji2TNJt2tEBlxPVFQBxvvk9xxsWwjmx49v%2FpAx1NPDGnxgGAGRRKU5u1JEWJfYGsdLeh5tmchHmNDtKyAY%2FPyOKgcPHRHO9oNpARpeRPtrjoonEOdhHd%2FS6ZvWKD1t%2Btv01ti5D9xP685OfWtFAVVY0oPWxmtz%2F500WxJfU4OZXEqhv14paeP4xrkAMoKxeNxfVvneX0mmL8ocSHDR9aMVdJbJm5IuQrmxWXoLDL1TjU%3D' 
swid = 'CC7CD84B-FAC5-47F2-95DA-3CAF524D7AC5'

# 2. Custom Photos mapped to exact names
CUSTOM_PHOTOS = {
    "Kyler Wilson": "kyler.jpg",
    "Samuel Reynolds": "samuel.jpg",
    "Joseph Bartoch": "joseph.jpg",
    "Matt Reynolds": "matt.jpg"
}

# 3. WEEKLY POWER RANKINGS 
POWER_RANKINGS_WEEK = "Pre-Draft Edition"
POWER_RANKINGS = [
    {
        "rank": 1,
        "manager": "Kyler Wilson",
        "change": "—",
        "status": "same", 
        "title": "Early Frontrunner",
        "blurb": "Confidence is high heading into the draft. Talk is cheap, but the roster strategy is dialed in."
    },
    {
        "rank": 2,
        "manager": "Matt Reynolds",
        "change": "—",
        "status": "same",
        "title": "Quiet Threat",
        "blurb": "Currently doing deep research on sleeper picks. Expect some bold moves in the middle rounds."
    },
    {
        "rank": 3,
        "manager": "Samuel Reynolds",
        "change": "—",
        "status": "same",
        "title": "Wildcard Contender",
        "blurb": "Nobody knows what the draft board looks like here, which makes this team dangerous."
    },
    {
        "rank": 4,
        "manager": "Joseph Bartoch",
        "change": "—",
        "status": "same",
        "title": "On Notice",
        "blurb": "Has the most to prove this season. Better make sure auto-draft is turned off."
    }
]

print("Connecting to ESPN...")
league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)

# 4. HTML, CSS, and JavaScript Setup
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Family Fantasy League</title>
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background-color: #f1f5f9; 
            color: #1e293b; 
            margin: 0; 
            padding: 30px 20px; 
        }
        
        .header-area {
            text-align: center;
            margin-bottom: 30px;
        }
        h1 { 
            margin: 0 0 6px 0; 
            color: #0f172a; 
            font-size: 4em; /* MASSIVE FONT SIZE FOR TESTING */
            font-weight: 900;
            letter-spacing: -1px;
        }
        .subtitle {
            color: #64748b;
            font-size: 1.05rem;
            margin: 0;
        }

        /* 3-COLUMN DASHBOARD GRID */
        .dashboard-grid { 
            max-width: 1450px; 
            margin: 0 auto; 
            display: grid;
            grid-template-columns: 1fr 1.15fr 1fr;
            gap: 24px;
            align-items: start;
        }

        @media (max-width: 1100px) {
            .dashboard-grid {
                grid-template-columns: 1fr;
            }
        }

        .column {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .section-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #e2e8f0;
            padding: 10px 16px;
            border-radius: 10px;
        }
        .section-badge {
            font-size: 0.75rem;
            background: #6366f1;
            color: white;
            padding: 3px 8px;
            border-radius: 999px;
            font-weight: 600;
        }

        /* POWER RANKINGS STYLING */
        .pr-card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            padding: 14px 16px;
            border-left: 4px solid #6366f1;
            display: flex;
            gap: 14px;
            align-items: flex-start;
        }
        .pr-rank-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-width: 38px;
        }
        .pr-number { font-size: 1.5rem; font-weight: 900; color: #0f172a; line-height: 1; }
        .pr-change { font-size: 0.7rem; font-weight: bold; margin-top: 3px; }
        .change-up { color: #16a34a; }
        .change-down { color: #dc2626; }
        .change-same { color: #94a3b8; }
        .pr-body { flex: 1; }
        .pr-header-line { display: flex; align-items: baseline; gap: 6px; margin-bottom: 3px; flex-wrap: wrap; }
        .pr-manager { font-size: 1.05rem; font-weight: 700; color: #0f172a; }
        .pr-tagline { font-size: 0.75rem; color: #6366f1; font-weight: 700; text-transform: uppercase; }
        .pr-blurb { margin: 0; color: #475569; font-size: 0.88rem; line-height: 1.4; }

        /* TEAM CARD STYLING */
        .card-wrapper {
            background: white; 
            border-radius: 10px; 
            box-shadow: 0 2px 6px rgba(0,0,0,0.05); 
            border-left: 4px solid #0284c7;
            transition: transform 0.15s ease;
            overflow: hidden; 
        }
        .card-wrapper:hover { transform: translateY(-2px); }
        .team-card-header { display: flex; align-items: center; padding: 12px 16px; cursor: pointer; background-color: white; user-select: none; }
        .team-card-header:hover { background-color: #f8fafc; }
        .arrow { margin-left: auto; color: #94a3b8; font-size: 1rem; font-weight: bold; }
        .logo { width: 56px; height: 56px; border-radius: 50%; object-fit: cover; border: 2px solid #e2e8f0; margin-right: 14px; flex-shrink: 0; }
        .text-info { display: flex; flex-direction: column; }
        .team-name { font-size: 1.1rem; font-weight: 700; margin: 0 0 2px 0; color: #0f172a; }
        .owner-name { margin: 0; color: #64748b; font-size: 0.85rem; }
        
        .dropdown-area { padding: 0 16px 16px 16px; background: #fafbfc; border-top: 1px solid #f1f5f9; }
        .tab-controls { display: flex; border-bottom: 2px solid #e2e8f0; margin-top: 8px; margin-bottom: 12px; }
        .tab-btn { flex: 1; background: none; border: none; padding: 8px; font-size: 0.85rem; font-weight: 600; color: #64748b; cursor: pointer; border-bottom: 2px solid transparent; outline: none; }
        .tab-btn:hover { color: #0284c7; }
        .tab-btn.active { color: #0284c7; border-bottom: 2px solid #0284c7; }
        .schedule-list, .roster-list { list-style: none; padding: 0; margin: 0; }
        .schedule-list li, .roster-list li { padding: 8px 0; border-bottom: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; font-size: 0.88rem; }
        .schedule-list li:last-child, .roster-list li:last-child { border-bottom: none; }
        
        .empty-state { justify-content: center !important; color: #94a3b8; font-style: italic; padding: 15px 0 !important; }
        .player-name { font-weight: 600; color: #1e293b; }
        .pos-badge { background: #e2e8f0; color: #475569; padding: 2px 8px; border-radius: 8px; font-size: 0.7rem; font-weight: 700; }
        .win { color: #16a34a; font-weight: bold; }
        .loss { color: #dc2626; font-weight: bold; }
        .tie { color: #4b5563; font-weight: bold; }
        .live-timer { color: #d97706; font-family: monospace; font-size: 0.82rem; font-weight: bold; }

        /* NEWS CARD STYLING */
        .news-card {
            display: flex;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            overflow: hidden;
            text-decoration: none;
            color: inherit;
            transition: transform 0.15s ease;
            border-left: 4px solid #dc2626;
        }
        .news-card:hover { transform: translateY(-2px); }
        .news-card img { width: 100px; height: 90px; object-fit: cover; }
        .news-info { padding: 10px 12px; flex: 1; display: flex; flex-direction: column; justify-content: center; }
        .news-info h4 { margin: 0 0 4px 0; font-size: 0.92rem; color: #0f172a; line-height: 1.3; }
        .news-info p { 
            margin: 0; font-size: 0.78rem; color: #64748b; line-height: 1.35;
            display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
        }
    </style>
    
    <script>
        function toggleDropdown(element) {
            var currentWrapper = element.closest('.card-wrapper');
            var currentDropdown = currentWrapper.querySelector('.dropdown-area');
            var currentArrow = element.querySelector('.arrow');
            var isCurrentlyOpen = (currentDropdown.style.display === "block");

            document.querySelectorAll('.card-wrapper').forEach(function(wrapper) {
                var dropdown = wrapper.querySelector('.dropdown-area');
                var arrow = wrapper.querySelector('.arrow');
                if (dropdown) dropdown.style.display = "none";
                if (arrow) arrow.innerHTML = "▼";
            });

            if (!isCurrentlyOpen) {
                currentDropdown.style.display = "block";
                currentArrow.innerHTML = "▲";
            }
        }
        
        function switchTab(btn, tabName) {
            var dropdownArea = btn.closest('.dropdown-area');
            dropdownArea.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            dropdownArea.querySelectorAll('.tab-content').forEach(c => c.style.display = 'none');
            dropdownArea.querySelector('.tab-' + tabName).style.display = 'block';
        }

        window.onload = function() {
            var baseKickoffDate = new Date("2026-09-13T13:00:00-04:00").getTime();
            setInterval(function() {
                var now = new Date().getTime();
                document.querySelectorAll('.live-timer').forEach(function(el) {
                    var weekIndex = parseInt(el.getAttribute('data-week'));
                    var kickoffTime = baseKickoffDate + (weekIndex * 7 * 24 * 60 * 60 * 1000);
                    var distance = kickoffTime - now;
                    
                    if (distance < 0) {
                        el.innerHTML = "Final / Live";
                        el.style.color = "#94a3b8";
                    } else {
                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
                        el.innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s";
                    }
                });
            }, 1000);

            fetch('https://site.api.espn.com/apis/site/v2/sports/football/nfl/news')
                .then(response => response.json())
                .then(data => {
                    var newsContainer = document.getElementById('news-container');
                    newsContainer.innerHTML = '';
                    var articles = data.articles.slice(0, 5);
                    
                    articles.forEach(function(article) {
                        var title = article.headline || "NFL News Update";
                        var desc = article.description || "Click to read more on ESPN.";
                        var link = (article.links && article.links.web && article.links.web.href) ? article.links.web.href : "https://www.espn.com/nfl/";
                        var img = (article.images && article.images.length > 0 && article.images[0].url) ? article.images[0].url : "https://a.espncdn.com/i/teamlogos/nfl/500/nfl.png";
                        
                        var card = document.createElement('a');
                        card.href = link;
                        card.target = '_blank';
                        card.className = 'news-card';
                        card.innerHTML = `
                            <img src="${img}" alt="News">
                            <div class="news-info">
                                <h4>${title}</h4>
                                <p>${desc}</p>
                            </div>
                        `;
                        newsContainer.appendChild(card);
                    });
                })
                .catch(error => {
                    document.getElementById('news-container').innerHTML = '<p style="text-align:center; color:#64748b; font-size:0.85rem;">Failed to load live news.</p>';
                });
        };
    </script>
</head>
<body>
    <div class="header-area">
        <h1>Bartoch Fantasy Football</h1>
        <div class="subtitle">Official League Dashboard</div>
    </div>
    
    <div class="dashboard-grid">
        
        <!-- COLUMN 1: POWER RANKINGS -->
        <div class="column">
            <div class="section-title">
                <span>⚡ Power Rankings</span>
                <span class="section-badge">{POWER_RANKINGS_WEEK}</span>
            </div>
"""

# Build Power Rankings HTML
for pr in POWER_RANKINGS:
    status_class = "change-same"
    if pr.get("status") == "up":
        status_class = "change-up"
    elif pr.get("status") == "down":
        status_class = "change-down"
        
    html_content += f"""
            <div class="pr-card">
                <div class="pr-rank-box">
                    <span class="pr-number">#{pr['rank']}</span>
                    <span class="pr-change {status_class}">{pr['change']}</span>
                </div>
                <div class="pr-body">
                    <div class="pr-header-line">
                        <span class="pr-manager">{pr['manager']}</span>
                        <span class="pr-tagline">• {pr['title']}</span>
                    </div>
                    <p class="pr-blurb">{pr['blurb']}</p>
                </div>
            </div>
    """

html_content += """
        </div>

        <!-- COLUMN 2: ROSTERS & SCHEDULES -->
        <div class="column">
            <div class="section-title">
                <span>🏈 Rosters & Schedules</span>
            </div>
"""

# Extract league data and build team cards
for team in league.teams:
    team_name = team.team_name
    
    if team.owners:
        first_owner = team.owners[0]
        if hasattr(first_owner, 'first_name'):
            owner_name = f"{first_owner.first_name} {first_owner.last_name}"
        elif isinstance(first_owner, dict):
            owner_name = f"{first_owner.get('firstName', '')} {first_owner.get('lastName', '')}".strip()
        else:
            owner_name = str(first_owner)
    else:
        owner_name = "Unknown Manager"

    logo = "https://a.espncdn.com/i/teamlogos/default-team-logo-500.png"
    if team.logo_url and team.logo_url != "":
        logo = team.logo_url
    for custom_name, filename in CUSTOM_PHOTOS.items():
        if custom_name.lower() == owner_name.lower():
            logo = filename
            break

    # Roster List
    roster_html = ""
    if len(team.roster) == 0:
        roster_html = "<li class='empty-state'>No players drafted yet.</li>"
    else:
        for player in team.roster:
            p_name = getattr(player, 'name', 'Unknown Player')
            p_pos = getattr(player, 'position', 'FLEX')
            roster_html += f"<li><span class='player-name'>{p_name}</span> <span class='pos-badge'>{p_pos}</span></li>"

    # Schedule List
    schedule_html = ""
    for week_num, opponent in enumerate(team.schedule):
        week_str = f"W{week_num + 1}"
        opp_name = opponent.team_name if hasattr(opponent, 'team_name') else "Bye"
            
        score = team.scores[week_num] if week_num < len(team.scores) else 0
        outcome = team.outcomes[week_num] if week_num < len(team.outcomes) else "U"
        
        if outcome == "W":
            res_html = f"<span class='win'>W ({score:.1f})</span>"
        elif outcome == "L":
            res_html = f"<span class='loss'>L ({score:.1f})</span>"
        elif outcome == "T":
            res_html = f"<span class='tie'>T ({score:.1f})</span>"
        else:
            res_html = f"<span class='live-timer' data-week='{week_num}'>...</span>"

        schedule_html += f"<li><span><strong>{week_str}:</strong> vs {opp_name}</span> {res_html}</li>"

    # Assemble Team Card
    html_content += f"""
            <div class="card-wrapper">
                <div class="team-card-header" onclick="toggleDropdown(this)">
                    <img src="{logo}" alt="{team_name}" class="logo">
                    <div class="text-info">
                        <p class="team-name">{team_name}</p>
                        <p class="owner-name">Manager: {owner_name}</p>
                    </div>
                    <div class="arrow">▼</div>
                </div>
                
                <div class="dropdown-area" style="display: none;">
                    <div class="tab-controls">
                        <button class="tab-btn active" onclick="switchTab(this, 'roster')">Roster</button>
                        <button class="tab-btn" onclick="switchTab(this, 'schedule')">Schedule</button>
                    </div>
                    
                    <div class="tab-content tab-roster" style="display: block;">
                        <ul class="roster-list">
                            {roster_html}
                        </ul>
                    </div>
                    
                    <div class="tab-content tab-schedule" style="display: none;">
                        <ul class="schedule-list">
                            {schedule_html}
                        </ul>
                    </div>
                </div>
            </div>
    """

html_content += """
        </div>

        <!-- COLUMN 3: RELEVANT NFL NEWS -->
        <div class="column">
            <div class="section-title">
                <span>📰 Relevant NFL News</span>
                <span class="section-badge" style="background:#dc2626;">Live</span>
            </div>
            <div id="news-container" class="column" style="gap: 12px;">
                <p style="text-align: center; color: #64748b; font-size: 0.85rem; padding: 15px;">Loading latest news...</p>
            </div>
        </div>

    </div> <!-- End Dashboard Grid -->
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Website updated! Refresh index.html in your browser.")