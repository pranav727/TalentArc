import os

BASE_CSS = """
:root {
  --primary: #6366F1;
  --primary-light: #818CF8;
  --primary-dark: #4F46E5;
  --accent: #06B6D4;
  --success: #10B981;
  --warning: #F59E0B;
  --error: #EF4444;
  --purple: #A855F7;
  --font: 'Inter', sans-serif;
  --r-sm: 8px;
  --r-md: 12px;
  --r-lg: 16px;
  --r-xl: 20px;
  --r-pill: 999px;
  --transition: 0.22s cubic-bezier(0.4, 0, 0.2, 1);
  --sidebar-w: 240px;
}

[data-theme="dark"] {
  --bg-base: #0A0A0F;
  --bg-1: #0F0F17;
  --bg-2: #13131E;
  --bg-3: #1A1A28;
  --bg-4: #1E1E2E;
  --bg-card: #15151F;
  --bg-hover: #252535;
  --text-1: #E2E8F0;
  --text-2: #94A3B8;
  --text-3: #64748B;
  --border: rgba(255,255,255,0.06);
  --border-2: rgba(255,255,255,0.10);
  --shadow: 0 4px 24px rgba(0,0,0,0.5);
  --glow: 0 0 20px rgba(99,102,241,0.15);
}

[data-theme="light"] {
  --bg-base: #F0F0F8;
  --bg-1: #FAFAFA;
  --bg-2: #FFFFFF;
  --bg-3: #F5F5FF;
  --bg-4: #EDEDFA;
  --bg-card: #FFFFFF;
  --bg-hover: #F0F0FF;
  --text-1: #0F172A;
  --text-2: #475569;
  --text-3: #94A3B8;
  --border: rgba(0,0,0,0.08);
  --border-2: rgba(0,0,0,0.12);
  --shadow: 0 4px 24px rgba(0,0,0,0.08);
  --glow: 0 0 20px rgba(99,102,241,0.08);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: var(--font);
  background: var(--bg-base);
  color: var(--text-1);
  min-height: 100vh;
  overflow-x: hidden;
  transition: background var(--transition), color var(--transition);
}
a { color: inherit; text-decoration: none; }
button { font-family: inherit; cursor: pointer; border: none; background: none; }
ul { list-style: none; }

.app-shell { display: flex; min-height: 100vh; }

.sidebar {
  width: var(--sidebar-w); flex-shrink: 0; position: fixed; top: 0; left: 0; bottom: 0;
  display: flex; flex-direction: column; background: var(--bg-2); border-right: 1px solid var(--border);
  z-index: 100; transition: transform var(--transition), background var(--transition); overflow: hidden;
}
.sidebar-logo {
  display: flex; align-items: center; gap: 10px; padding: 22px 18px 20px;
  border-bottom: 1px solid var(--border);
}
.logo-icon {
  width: 34px; height: 34px; background: linear-gradient(135deg, var(--primary), var(--purple));
  border-radius: 10px; display: flex; align-items: center; justify-content: center;
  font-size: 16px; color: #fff; box-shadow: 0 4px 12px rgba(99,102,241,0.4); flex-shrink: 0;
}
.logo-text {
  font-size: 15px; font-weight: 700; letter-spacing: -0.3px;
  background: linear-gradient(135deg, var(--primary-light), var(--purple));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.sidebar-nav { flex: 1; padding: 12px 10px; overflow-y: auto; }
.nav-section-label {
  font-size: 10px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--text-3);
  padding: 12px 10px 6px;
}
.nav-item {
  display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: var(--r-sm);
  color: var(--text-2); font-size: 13.5px; font-weight: 500; cursor: pointer;
  transition: all var(--transition); position: relative; margin-bottom: 2px;
}
.nav-item:hover { background: var(--bg-hover); color: var(--text-1); }
.nav-item.active { background: rgba(99,102,241,0.15); color: var(--primary-light); font-weight: 600; }
.nav-item.active::before {
  content: ''; position: absolute; left: 0; top: 20%; bottom: 20%; width: 3px;
  background: linear-gradient(180deg, var(--primary), var(--purple)); border-radius: 0 3px 3px 0;
}
.nav-icon { font-size: 15px; flex-shrink: 0; width: 20px; text-align: center; }
.nav-label { flex: 1; }
.nav-badge { font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: var(--r-pill); line-height: 1.4; }
.badge-number { background: var(--error); color: #fff; }
.badge-new { background: linear-gradient(135deg, var(--primary), var(--purple)); color: #fff; font-size: 9px; }

.sidebar-profile {
  padding: 14px 14px 18px; border-top: 1px solid var(--border);
  display: flex; align-items: center; gap: 10px; cursor: pointer; transition: background var(--transition);
}
.sidebar-profile:hover { background: var(--bg-hover); }
.profile-avatar {
  width: 36px; height: 36px; border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--purple));
  display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; color: #fff;
  flex-shrink: 0; border: 2px solid rgba(99,102,241,0.4);
}
.profile-info { flex: 1; min-width: 0; }
.profile-name { font-size: 12.5px; font-weight: 600; color: var(--text-1); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.profile-role { font-size: 11px; color: var(--text-3); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

.main-area { flex: 1; margin-left: var(--sidebar-w); display: flex; flex-direction: column; min-height: 100vh; }
.top-header {
  position: sticky; top: 0; z-index: 90; background: rgba(10,10,15,0.75); backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px); border-bottom: 1px solid var(--border); padding: 0 28px;
  height: 66px; display: flex; align-items: center; gap: 20px; transition: background var(--transition);
}
[data-theme="light"] .top-header { background: rgba(250,250,250,0.85); }
.header-greeting { flex: 1; }
.header-greeting h1 { font-size: 16px; font-weight: 700; color: var(--text-1); letter-spacing: -0.2px; }
.header-greeting p { font-size: 12px; color: var(--text-2); margin-top: 1px; }
.header-actions { display: flex; align-items: center; gap: 8px; }
.icon-btn {
  width: 36px; height: 36px; border-radius: var(--r-sm); display: flex; align-items: center; justify-content: center;
  color: var(--text-2); background: var(--bg-3); border: 1px solid var(--border); cursor: pointer; transition: all var(--transition);
  position: relative;
}
.icon-btn:hover { background: var(--bg-4); color: var(--text-1); border-color: var(--border-2); }
.notif-dot {
  position: absolute; top: 6px; right: 6px; width: 8px; height: 8px; background: var(--error);
  border-radius: 50%; border: 1.5px solid var(--bg-2);
}

.page-content { padding: 24px 28px; flex: 1; display: flex; flex-direction: column; gap: 20px; animation: fadeIn 0.25s ease-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

.content-grid { display: grid; grid-template-columns: 1fr 340px; gap: 20px; align-items: start; }
.card {
  background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 20px;
  transition: box-shadow var(--transition), border-color var(--transition), transform var(--transition);
}
.card:hover { box-shadow: var(--glow), var(--shadow); border-color: var(--border-2); }
.card-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; }
.card-title { font-size: 14.5px; font-weight: 700; color: var(--text-1); display: flex; align-items: center; gap: 8px; }

.btn {
  padding: 10px 18px; border-radius: var(--r-pill); font-size: 13px; font-weight: 600; display: inline-flex;
  align-items: center; gap: 6px; transition: all var(--transition); cursor: pointer;
}
.btn-primary { background: linear-gradient(135deg, var(--primary), var(--primary-light)); color: #fff; }
.btn-primary:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(99,102,241,0.3); }
.btn-secondary { border: 1px solid var(--border); color: var(--text-2); background: var(--bg-3); }
.btn-secondary:hover { border-color: var(--border-2); color: var(--text-1); background: var(--bg-hover); }

.form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 14px; }
.form-group { display: flex; flex-direction: column; gap: 6px; }
.form-label { font-size: 12.5px; font-weight: 600; color: var(--text-2); }
.form-input {
  width: 100%; padding: 10px 14px; background: var(--bg-3); border: 1px solid var(--border);
  border-radius: var(--r-md); color: var(--text-1); font-family: inherit; font-size: 13.5px; outline: none;
  transition: all var(--transition);
}
.form-input:focus { border-color: var(--primary); background: var(--bg-4); box-shadow: 0 0 0 3px rgba(99,102,241,0.15); }
.form-input-full { grid-column: span 2; }

.badge { display: inline-flex; align-items: center; gap: 4px; padding: 4px 10px; border-radius: var(--r-pill); font-size: 11px; font-weight: 600; }
.badge-success { background: rgba(16,185,129,0.12); color: var(--success); border: 1px solid rgba(16,185,129,0.2); }
.badge-warning { background: rgba(245,158,11,0.12); color: var(--warning); border: 1px solid rgba(245,158,11,0.2); }
.badge-error { background: rgba(239,68,68,0.12); color: var(--error); border: 1px solid rgba(239,68,68,0.2); }

.skeleton-overlay {
  position: fixed; inset: 0; background: var(--bg-base); z-index: 1000;
  display: flex; align-items: center; justify-content: center;
  transition: opacity 0.4s ease, visibility 0.4s ease;
}
.skeleton-overlay.hide { opacity: 0; visibility: hidden; pointer-events: none; }
@keyframes shimmer { 0% { transform: translateX(-100%); } 100% { transform: translateX(100%); } }

@media (max-width: 900px) {
  .sidebar { transform: translateX(-100%); }
  .main-area { margin-left: 0; }
  .top-header { padding: 0 16px; }
  .page-content { padding: 16px; }
  .content-grid { grid-template-columns: 1fr; }
}
"""

# Seeker Navigation Settings
SEEKER_NAV = [
    {"id": "overview", "label": "Dashboard", "icon": "layout-dashboard", "url": "dashboard.html"},
    {"id": "profile", "label": "My Profile", "icon": "user", "url": "profile.html"},
    {"id": "resume", "label": "Resume Center", "icon": "file-text", "url": "resume.html"},
    {"id": "jobs", "label": "Job Search", "icon": "search", "url": "jobs.html"},
    {"id": "saved-jobs", "label": "Saved Jobs", "icon": "heart", "url": "saved-jobs.html"},
    {"id": "interviews", "label": "Interview Center", "icon": "calendar", "url": "interviews.html"},
    {"id": "messages", "label": "Messages", "icon": "message-square", "url": "messages.html", "badge": "3", "badge_class": "badge-number"},
    {"id": "ai-career", "label": "AI Career Center", "icon": "sparkles", "url": "ai-tools.html", "badge": "NEW", "badge_class": "badge-new"},
    {"id": "analytics", "label": "Career Insights", "icon": "bar-chart-2", "url": "career-insights.html"},
    {"id": "settings", "label": "Settings & Security", "icon": "settings", "url": "settings.html"},
]

# Employer Navigation Settings
EMPLOYER_NAV = [
    {"id": "dashboard", "label": "Dashboard", "icon": "layout-dashboard", "url": "dashboard.html"},
    {"id": "post-job", "label": "Post Job", "icon": "plus-circle", "url": "post-job.html"},
    {"id": "manage-jobs", "label": "Manage Jobs", "icon": "briefcase", "url": "manage-jobs.html"},
    {"id": "applicants", "label": "Applicants", "icon": "users", "url": "applicants.html"},
    {"id": "company-profile", "label": "Company Profile", "icon": "building", "url": "company-profile.html"},
    {"id": "messages", "label": "Messages", "icon": "message-square", "url": "messages.html"},
    {"id": "analytics", "label": "Hiring Analytics", "icon": "bar-chart-2", "url": "analytics.html"},
    {"id": "settings", "label": "Settings", "icon": "settings", "url": "settings.html"},
]

# Recruiter Navigation Settings
RECRUITER_NAV = [
    {"id": "dashboard", "label": "Dashboard", "icon": "layout-dashboard", "url": "dashboard.html"},
    {"id": "candidates", "label": "Candidates", "icon": "users", "url": "candidates.html"},
    {"id": "pipeline", "label": "Pipeline Analytics", "icon": "activity", "url": "pipeline.html"},
    {"id": "messages", "label": "Messages", "icon": "message-square", "url": "messages.html"},
    {"id": "settings", "label": "Settings", "icon": "settings", "url": "dashboard.html"},
]

# Admin Navigation Settings
ADMIN_NAV = [
    {"id": "dashboard", "label": "Dashboard", "icon": "layout-dashboard", "url": "dashboard.html"},
    {"id": "users", "label": "User Management", "icon": "users", "url": "users.html"},
    {"id": "jobs", "label": "Jobs Moderation", "icon": "check-square", "url": "jobs.html"},
    {"id": "reports", "label": "Reports & Logs", "icon": "shield-alert", "url": "reports.html"},
    {"id": "settings", "label": "System Settings", "icon": "settings", "url": "settings.html"},
]

def generate_page(filepath, role, title, sidebar_items, active_id, user_initials, user_name, user_role, main_content, custom_css="", custom_script=""):
    sidebar_html = ""
    if sidebar_items:
        for item in sidebar_items:
            is_active = " active" if item["id"] == active_id else ""
            badge_html = f'<span class="nav-badge {item["badge_class"]}">{item["badge"]}</span>' if "badge" in item else ""
            sidebar_html += f'''
          <a href="{item["url"]}" class="nav-item{is_active}" id="nav-{item["id"]}">
            <i data-lucide="{item["icon"]}" class="nav-icon"></i>
            <span class="nav-label">{item["label"]}</span>
            {badge_html}
          </a>
    '''

    if not sidebar_items:
        layout = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>TalentArc · {title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
  <style>
    {BASE_CSS}
    .topbar {{
      display: flex; align-items: center; justify-content: space-between; padding: 16px 40px;
      background: rgba(10,10,15,0.75); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border);
      position: sticky; top: 0; z-index: 100;
    }}
    [data-theme="light"] .topbar {{ background: rgba(250,250,250,0.85); }}
    .topbar-logo {{ display: flex; align-items: center; gap: 8px; font-weight: 800; font-size: 18px; }}
    .topbar-links {{ display: flex; gap: 24px; align-items: center; }}
    .topbar-links a {{ font-size: 14.5px; font-weight: 500; color: var(--text-2); transition: color var(--transition); }}
    .topbar-links a:hover {{ color: var(--primary-light); }}
    .topbar-actions {{ display: flex; align-items: center; gap: 14px; }}
    .public-footer {{ background: var(--bg-2); border-top: 1px solid var(--border); padding: 56px 40px 24px; margin-top: 56px; }}
    .footer-grid {{ display: grid; grid-template-columns: 2fr repeat(4, 1fr); gap: 40px; max-width: 1200px; margin: 0 auto; }}
    .footer-col h4 {{ font-size: 13px; font-weight: 700; color: var(--text-1); text-transform: uppercase; margin-bottom: 16px; letter-spacing: 0.05em; }}
    .footer-col ul {{ display: flex; flex-direction: column; gap: 10px; }}
    .footer-col ul a {{ font-size: 13.5px; color: var(--text-2); transition: color var(--transition); }}
    .footer-col ul a:hover {{ color: var(--primary-light); }}
    {custom_css}
  </style>
</head>
<body>
<div class="skeleton-overlay" id="skeletonOverlay">
  <div style="text-align:center; color: var(--text-2);">
    <div style="font-size: 28px; font-weight:700; color:var(--primary-light); margin-bottom:10px;">✦ TalentArc</div>
    <div style="width: 80px; height: 3px; background:var(--border); border-radius:var(--r-pill); overflow:hidden; margin:0 auto; position:relative;">
      <div style="width: 40%; height:100%; background:var(--primary); position:absolute; left:0; top:0; animation: shimmer 1.5s infinite linear;"></div>
    </div>
  </div>
</div>

<header class="topbar">
  <a href="../index.html" class="topbar-logo">
    <div class="logo-icon" style="width:30px; height:30px; font-size:14px;">✦</div>
    <span class="logo-text">TalentArc</span>
  </a>
  <nav class="topbar-links">
    <a href="job-details.html">Find Jobs</a>
    <a href="companies.html">Companies</a>
    <a href="resources.html">Resources</a>
    <a href="../seeker/dashboard.html">Dashboard</a>
  </nav>
  <div class="topbar-actions">
    <button class="icon-btn" id="themeToggle"><i data-lucide="sun" id="themeIcon" style="width: 18px; height: 18px;"></i></button>
    <a href="../auth/login.html" class="btn btn-secondary" style="padding: 8px 16px; font-size:13px; border-radius:var(--r-md);">Sign In</a>
    <a href="../auth/register.html" class="btn btn-primary" style="padding: 8px 16px; font-size:13px; border-radius:var(--r-md);">Get Started</a>
  </div>
</header>

<main style="min-height: calc(100vh - 200px);">
  {main_content}
</main>

<footer class="public-footer">
  <div class="footer-grid">
    <div class="footer-col">
      <div class="topbar-logo" style="margin-bottom:12px;">
        <div class="logo-icon" style="width:28px; height:28px; font-size:13px;">✦</div>
        <span class="logo-text">TalentArc</span>
      </div>
      <p style="font-size:13px; color:var(--text-3); line-height:1.6; max-width:240px;">World-class, AI-driven recruitment and career accelerator platform built for next-generation talent.</p>
    </div>
    <div class="footer-col">
      <h4>For Candidates</h4>
      <ul>
        <li><a href="../seeker/dashboard.html">Explore Dashboard</a></li>
        <li><a href="job-details.html">Smart Job Search</a></li>
        <li><a href="../seeker/resume.html">AI Resume Builder</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>For Employers</h4>
      <ul>
        <li><a href="../employer/dashboard.html">Post a Job</a></li>
        <li><a href="../employer/applicants.html">ATS Pipeline</a></li>
        <li><a href="../employer/analytics.html">Hiring Analytics</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Company</h4>
      <ul>
        <li><a href="#">About Us</a></li>
        <li><a href="#">Careers</a></li>
        <li><a href="#">Press</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Resources</h4>
      <ul>
        <li><a href="resources.html">Blog Guides</a></li>
        <li><a href="../public/salary-insights.html">Salary Calculator</a></li>
        <li><a href="#">Support Center</a></li>
      </ul>
    </div>
  </div>
  <div style="text-align:center; margin-top:40px; padding-top:20px; border-top:1px solid var(--border); font-size:12.5px; color:var(--text-3);">
    &copy; 2026 TalentArc Inc. All rights reserved.
  </div>
</footer>

<script>
  lucide.createIcons();
  window.addEventListener('load', () => {{
    setTimeout(() => {{ document.getElementById('skeletonOverlay').classList.add('hide'); }}, 300);
  }});
  const themeToggle = document.getElementById('themeToggle');
  const themeIcon = document.getElementById('themeIcon');
  const htmlEl = document.documentElement;
  const savedTheme = localStorage.getItem('theme') || 'dark';
  htmlEl.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);
  themeToggle.addEventListener('click', () => {{
    const currentTheme = htmlEl.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    htmlEl.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
  }});
  function updateThemeIcon(theme) {{
    if (theme === 'dark') {{ themeIcon.setAttribute('data-lucide', 'sun'); }}
    else {{ themeIcon.setAttribute('data-lucide', 'moon'); }}
    lucide.createIcons();
  }}
  {custom_script}
</script>
</body>
</html>
"""
    else:
        layout = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>TalentArc · {title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
  <style>
    {BASE_CSS}
    {custom_css}
  </style>
</head>
<body>
<div class="skeleton-overlay" id="skeletonOverlay">
  <div style="text-align:center; color: var(--text-2);">
    <div style="font-size: 28px; font-weight:700; color:var(--primary-light); margin-bottom:10px;">✦ TalentArc</div>
    <div style="width: 80px; height: 3px; background:var(--border); border-radius:var(--r-pill); overflow:hidden; margin:0 auto; position:relative;">
      <div style="width: 40%; height:100%; background:var(--primary); position:absolute; left:0; top:0; animation: shimmer 1.5s infinite linear;"></div>
    </div>
  </div>
</div>

<div class="app-shell">
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-logo">
      <div class="logo-icon">✦</div>
      <span class="logo-text">TalentArc</span>
    </div>
    <nav class="sidebar-nav">
      <div class="nav-section-label">{role} Portal</div>
      {sidebar_html}
    </nav>
    <div class="sidebar-profile">
      <div class="profile-avatar">{user_initials}</div>
      <div class="profile-info">
        <div class="profile-name">{user_name}</div>
        <div class="profile-role">{user_role}</div>
      </div>
    </div>
  </aside>

  <div class="main-area">
    <header class="top-header">
      <div class="header-greeting">
        <h1>{title}</h1>
        <p>Premium platform workspace · Role: {role}</p>
      </div>
      <div class="header-actions">
        <button class="icon-btn" id="themeToggle" aria-label="Toggle Theme">
          <i data-lucide="sun" id="themeIcon" style="width: 18px; height: 18px;"></i>
        </button>
        <button class="icon-btn" aria-label="Notifications">
          <i data-lucide="bell" style="width: 18px; height: 18px;"></i>
          <span class="notif-dot"></span>
        </button>
        <div class="header-avatar">{user_initials}</div>
      </div>
    </header>

    <main class="page-content">
      {main_content}
    </main>
  </div>
</div>

<script>
  lucide.createIcons();
  window.addEventListener('load', () => {{
    setTimeout(() => {{ document.getElementById('skeletonOverlay').classList.add('hide'); }}, 300);
  }});
  const themeToggle = document.getElementById('themeToggle');
  const themeIcon = document.getElementById('themeIcon');
  const htmlEl = document.documentElement;
  const savedTheme = localStorage.getItem('theme') || 'dark';
  htmlEl.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);
  themeToggle.addEventListener('click', () => {{
    const currentTheme = htmlEl.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    htmlEl.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
  }});
  function updateThemeIcon(theme) {{
    if (theme === 'dark') {{ themeIcon.setAttribute('data-lucide', 'sun'); }}
    else {{ themeIcon.setAttribute('data-lucide', 'moon'); }}
    lucide.createIcons();
  }}
  {custom_script}
</script>
</body>
</html>
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(layout)

# Create folders
os.makedirs("seeker", exist_ok=True)
os.makedirs("employer", exist_ok=True)
os.makedirs("recruiter", exist_ok=True)
os.makedirs("admin", exist_ok=True)
os.makedirs("public", exist_ok=True)

# ----------------------------------------------------
# SEEKER PAGES DEFINITION
# ----------------------------------------------------
seeker_profile_main = """
<div class="content-grid">
  <div class="left-col" style="display:flex; flex-direction:column; gap:20px;">
    <div class="card" style="display:flex; gap:20px; align-items:center;">
      <div class="profile-avatar" style="width:80px; height:80px; font-size:32px; border:3px solid rgba(99,102,241,0.4); border-radius:50%;">PS</div>
      <div style="flex:1;">
        <h2 style="font-size:20px; font-weight:700;">Priya Sharma</h2>
        <p style="font-size:14px; color:var(--text-2);">Senior Software Engineer · Distributed Systems & React</p>
        <span class="badge badge-success" style="margin-top:8px;">🟢 Open to Work (Remote, Hybrid)</span>
      </div>
    </div>
    <div class="card">
      <h3 class="card-title" style="margin-bottom:12px;"><i data-lucide="user" style="color:var(--primary); width:18px;"></i> Personal Details</h3>
      <div class="form-grid">
        <div class="form-group"><label class="form-label">Full Name</label><input type="text" class="form-input" value="Priya Sharma" /></div>
        <div class="form-group"><label class="form-label">Email Address</label><input type="email" class="form-input" value="priya.sharma@gmail.com" /></div>
        <div class="form-group"><label class="form-label">Phone Number</label><input type="text" class="form-input" value="+1 (555) 019-2834" /></div>
        <div class="form-group"><label class="form-label">Location</label><input type="text" class="form-input" value="San Francisco, CA" /></div>
      </div>
    </div>
  </div>
  <div class="right-col">
    <div class="card">
      <h3 class="card-title">Profile Strength: 72%</h3>
      <div style="background:var(--bg-3); border-radius:var(--r-pill); height:6px; overflow:hidden; margin:10px 0;">
        <div style="background:linear-gradient(90deg, var(--primary), var(--accent)); width:72%; height:100%;"></div>
      </div>
      <button class="btn btn-primary" style="width:100%; margin-top:8px;" onclick="alert('Profile updated!')">Save Profile</button>
    </div>
  </div>
</div>
"""
generate_page("seeker/profile.html", "Job Seeker", "My Profile", SEEKER_NAV, "profile", "PS", "Priya Sharma", "Software Engineer", seeker_profile_main)

seeker_saved_jobs_main = """
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
  <h2 style="font-size:18px; font-weight:700;">Saved Jobs (18)</h2>
</div>
<div style="display:grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap:16px;">
  <div class="card" style="display:flex; flex-direction:column; justify-content:space-between; min-height:160px;">
    <div>
      <div style="display:flex; justify-content:space-between;">
        <h4 style="font-weight:700;">Senior Software Engineer</h4>
        <i data-lucide="heart" style="color:var(--error); fill:var(--error); width:18px; cursor:pointer;"></i>
      </div>
      <p style="font-size:12.5px; color:var(--text-2);">Stripe · SF / Hybrid</p>
    </div>
    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--border); padding-top:10px; margin-top:12px;">
      <span style="font-weight:700;">$180K - $240K</span>
      <a href="apply.html" class="btn btn-primary" style="padding:6px 12px; font-size:12px;">Apply</a>
    </div>
  </div>
  <div class="card" style="display:flex; flex-direction:column; justify-content:space-between; min-height:160px;">
    <div>
      <div style="display:flex; justify-content:space-between;">
        <h4 style="font-weight:700;">Staff Engineer</h4>
        <i data-lucide="heart" style="color:var(--error); fill:var(--error); width:18px; cursor:pointer;"></i>
      </div>
      <p style="font-size:12.5px; color:var(--text-2);">Vercel · Remote</p>
    </div>
    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--border); padding-top:10px; margin-top:12px;">
      <span style="font-weight:700;">$200K - $260K</span>
      <a href="apply.html" class="btn btn-primary" style="padding:6px 12px; font-size:12px;">Apply</a>
    </div>
  </div>
</div>
"""
generate_page("seeker/saved-jobs.html", "Job Seeker", "Saved Jobs", SEEKER_NAV, "saved-jobs", "PS", "Priya Sharma", "Software Engineer", seeker_saved_jobs_main)

seeker_interviews_main = """
<div class="content-grid">
  <div class="left-col" style="display:flex; flex-direction:column; gap:20px;">
    <div class="card">
      <h3 class="card-title" style="margin-bottom:12px;"><i data-lucide="calendar"></i> Upcoming Interviews</h3>
      <div style="display:flex; gap:16px; border:1px solid var(--border); border-radius:var(--r-md); padding:16px; background:var(--bg-3); align-items:center;">
        <div class="profile-avatar" style="width:48px; height:48px; background:#4F46E5; font-weight:800; border-radius:50%;">S</div>
        <div style="flex:1;">
          <h4 style="font-size:14.5px; font-weight:700;">Senior SWE — Technical Loop</h4>
          <p style="font-size:12px; color:var(--text-2);">Stripe · Tomorrow 10:00 AM PST</p>
        </div>
        <button class="btn btn-primary" style="padding:8px 14px;" onclick="alert('Launching meeting...')">Join Call</button>
      </div>
    </div>
  </div>
</div>
"""
generate_page("seeker/interviews.html", "Job Seeker", "Interview Center", SEEKER_NAV, "interviews", "PS", "Priya Sharma", "Software Engineer", seeker_interviews_main)

seeker_insights_main = """
<div style="display:grid; grid-template-columns: repeat(4, 1fr); gap:16px; margin-bottom:20px;">
  <div class="card" style="border-top: 3px solid var(--primary);"><p style="font-size:12.5px; color:var(--text-3);">Profile Views</p><h3>312</h3></div>
  <div class="card" style="border-top: 3px solid var(--accent);"><p style="font-size:12.5px; color:var(--text-3);">Resume Downloads</p><h3>48</h3></div>
  <div class="card" style="border-top: 3px solid var(--success);"><p style="font-size:12.5px; color:var(--text-3);">Search Appearances</p><h3>1,240</h3></div>
  <div class="card" style="border-top: 3px solid var(--purple);"><p style="font-size:12.5px; color:var(--text-3);">Hiring Rate</p><h3>92% Match</h3></div>
</div>
"""
generate_page("seeker/career-insights.html", "Job Seeker", "Career Insights", SEEKER_NAV, "analytics", "PS", "Priya Sharma", "Software Engineer", seeker_insights_main)

seeker_settings_main = """
<div class="content-grid">
  <div class="left-col" style="display:flex; flex-direction:column; gap:20px;">
    <div class="card">
      <h3 class="card-title">Account Preferences</h3>
      <div class="form-grid">
        <div class="form-group"><label class="form-label">Theme Mode</label>
          <select class="form-input" onchange="document.documentElement.setAttribute('data-theme', this.value); localStorage.setItem('theme', this.value);">
            <option value="dark">Dark Theme</option>
            <option value="light">Light Theme</option>
          </select>
        </div>
      </div>
    </div>
  </div>
</div>
"""
generate_page("seeker/settings.html", "Job Seeker", "Settings", SEEKER_NAV, "settings", "PS", "Priya Sharma", "Software Engineer", seeker_settings_main)

seeker_resume_main = """
<div class="content-grid">
  <div class="left-col" style="display:flex; flex-direction:column; gap:20px;">
    <div class="card" style="border: 2px dashed var(--border); text-align:center; padding:40px 20px;">
      <i data-lucide="upload-cloud" style="width:48px; height:48px; color:var(--primary-light); margin:0 auto 12px;"></i>
      <h4>Drag &amp; Drop Resume File</h4>
    </div>
  </div>
</div>
"""
generate_page("seeker/resume.html", "Job Seeker", "Resume Center", SEEKER_NAV, "resume", "PS", "Priya Sharma", "Software Engineer", seeker_resume_main)

# ----------------------------------------------------
# EMPLOYER PAGES DEFINITION
# ----------------------------------------------------
employer_manage_jobs = """
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
  <h2>Manage Postings</h2>
  <a href="post-job.html" class="btn btn-primary">Post New Job</a>
</div>
<div class="card">
  <div style="overflow-x:auto;">
    <table style="width:100%; border-collapse:collapse; text-align:left; font-size:13.5px;">
      <thead>
        <tr style="border-bottom:1px solid var(--border); color:var(--text-3);">
          <th style="padding:12px;">Job Title</th>
          <th style="padding:12px;">Candidates</th>
          <th style="padding:12px;">Status</th>
          <th style="padding:12px;">Posted Date</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom:1px solid var(--border);">
          <td style="padding:12px; font-weight:600;">Senior Software Engineer</td>
          <td style="padding:12px;">47 applicants</td>
          <td style="padding:12px;"><span class="badge badge-success">Active</span></td>
          <td style="padding:12px;">Jan 5, 2025</td>
        </tr>
        <tr style="border-bottom:1px solid var(--border);">
          <td style="padding:12px; font-weight:600;">Product Designer</td>
          <td style="padding:12px;">32 applicants</td>
          <td style="padding:12px;"><span class="badge badge-success">Active</span></td>
          <td style="padding:12px;">Jan 3, 2025</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""
generate_page("employer/manage-jobs.html", "Employer", "Manage Jobs", EMPLOYER_NAV, "manage-jobs", "TC", "TechCorp Inc", "Hiring Team", employer_manage_jobs)

employer_analytics = """
<div style="display:grid; grid-template-columns: repeat(4, 1fr); gap:16px; margin-bottom:20px;">
  <div class="card"><h5>Total Applications</h5><h3>342</h3></div>
  <div class="card"><h5>Time to Hire</h5><h3>23 Days</h3></div>
  <div class="card"><h5>Offer Rate</h5><h3>78%</h3></div>
  <div class="card"><h5>Active Openings</h5><h3>12 Roles</h3></div>
</div>
<div class="card">
  <h3 class="card-title">Hiring funnel</h3>
  <div style="display:flex; flex-direction:column; gap:12px; margin-top:20px;">
    <div>Applied (342) <div style="background:var(--bg-3); height:16px; border-radius:8px;"><div style="background:var(--primary); width:100%; height:100%; border-radius:8px;"></div></div></div>
    <div>Offered (18) <div style="background:var(--bg-3); height:16px; border-radius:8px;"><div style="background:var(--accent); width:20%; height:100%; border-radius:8px;"></div></div></div>
  </div>
</div>
"""
generate_page("employer/analytics.html", "Employer", "Analytics", EMPLOYER_NAV, "analytics", "TC", "TechCorp Inc", "Hiring Team", employer_analytics)

employer_messages = """
<div style="display:grid; grid-template-columns: 300px 1fr; gap:20px; height:500px;">
  <div class="card" style="padding:12px; display:flex; flex-direction:column; gap:10px;">
    <h3>Inbox</h3>
    <div style="background:var(--bg-3); padding:10px; border-radius:var(--r-md); cursor:pointer;">
      <strong>Alex Chen</strong>
      <p style="font-size:12px; color:var(--text-3);">Sent portfolio links...</p>
    </div>
  </div>
  <div class="card" style="display:flex; flex-direction:column; justify-content:space-between;">
    <div>
      <div style="border-bottom:1px solid var(--border); padding-bottom:12px; margin-bottom:12px;"><strong>Alex Chen</strong> · Frontend Applicant</div>
      <div style="font-size:13.5px; color:var(--text-2);">"Hello, I am excited about the Frontend Engineer role at TechCorp. Here is my portfolio website."</div>
    </div>
    <div style="display:flex; gap:10px;"><input type="text" class="form-input" placeholder="Write reply..." /><button class="btn btn-primary">Send</button></div>
  </div>
</div>
"""
generate_page("employer/messages.html", "Employer", "Candidate Messages", EMPLOYER_NAV, "messages", "TC", "TechCorp Inc", "Hiring Team", employer_messages)

employer_settings = """
<div class="content-grid">
  <div class="left-col" style="display:flex; flex-direction:column; gap:20px;">
    <div class="card">
      <h3 class="card-title">Company Profile Details</h3>
      <div class="form-grid">
        <div class="form-group"><label class="form-label">Legal Name</label><input type="text" class="form-input" value="TechCorp Inc" /></div>
        <div class="form-group"><label class="form-label">Website</label><input type="text" class="form-input" value="https://techcorp.com" /></div>
      </div>
    </div>
  </div>
</div>
"""
generate_page("employer/settings.html", "Employer", "Account Settings", EMPLOYER_NAV, "settings", "TC", "TechCorp Inc", "Hiring Team", employer_settings)


# ----------------------------------------------------
# RECRUITER PAGES DEFINITION
# ----------------------------------------------------
recruiter_candidates = """
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
  <h2>Candidate Board</h2>
</div>
<div style="display:grid; grid-template-columns: repeat(4, 1fr); gap:16px;">
  <div class="card" style="background:var(--bg-3);">
    <h4 style="margin-bottom:12px;">New (4)</h4>
    <div class="card" style="margin-bottom:8px;"><strong>James Liu</strong><p style="font-size:11px; color:var(--text-3);">Staff SWE · 95% Match</p></div>
    <div class="card"><strong>Sarah Kim</strong><p style="font-size:11px; color:var(--text-3);">Designer · 91% Match</p></div>
  </div>
  <div class="card" style="background:var(--bg-3);">
    <h4 style="margin-bottom:12px;">Screening (2)</h4>
    <div class="card"><strong>Maria Garcia</strong><p style="font-size:11px; color:var(--text-3);">SWE · 93% Match</p></div>
  </div>
  <div class="card" style="background:var(--bg-3);">
    <h4 style="margin-bottom:12px;">Interview (1)</h4>
    <div class="card"><strong>Emily Wang</strong><p style="font-size:11px; color:var(--text-3);">Data Scientist · 94% Match</p></div>
  </div>
  <div class="card" style="background:var(--bg-3);">
    <h4 style="margin-bottom:12px;">Offer (1)</h4>
    <div class="card"><strong>Lisa Zhang</strong><p style="font-size:11px; color:var(--text-3);">SWE · 97% Match</p></div>
  </div>
</div>
"""
generate_page("recruiter/candidates.html", "Recruiter", "Candidate Board", RECRUITER_NAV, "candidates", "AM", "Alex Morrison", "Senior Recruiter", recruiter_candidates)

recruiter_pipeline = """
<div class="card">
  <h3 class="card-title">Recruitment Pipeline Analytics</h3>
  <div style="display:flex; flex-direction:column; gap:12px; margin-top:20px;">
    <div>Sourced (156) <div style="background:var(--bg-3); height:16px; border-radius:8px;"><div style="background:var(--primary); width:100%; height:100%; border-radius:8px;"></div></div></div>
    <div>Interviewed (28) <div style="background:var(--bg-3); height:16px; border-radius:8px;"><div style="background:var(--accent); width:18%; height:100%; border-radius:8px;"></div></div></div>
    <div>Hired (10) <div style="background:var(--bg-3); height:16px; border-radius:8px;"><div style="background:var(--success); width:6%; height:100%; border-radius:8px;"></div></div></div>
  </div>
</div>
"""
generate_page("recruiter/pipeline.html", "Recruiter", "Pipeline Stats", RECRUITER_NAV, "pipeline", "AM", "Alex Morrison", "Senior Recruiter", recruiter_pipeline)

recruiter_messages = """
<div style="display:grid; grid-template-columns: 280px 1fr; gap:20px; height:500px;">
  <div class="card" style="padding:12px;">
    <h3>Direct Messages</h3>
    <div style="background:var(--bg-3); padding:10px; border-radius:var(--r-md); margin-top:10px; cursor:pointer;">
      <strong>James Liu</strong>
      <p style="font-size:12px; color:var(--text-3);">Interview scheduled confirm...</p>
    </div>
  </div>
  <div class="card" style="display:flex; flex-direction:column; justify-content:space-between;">
    <div><strong>James Liu</strong> · Staff SWE candidate</div>
    <div style="display:flex; gap:10px;"><input type="text" class="form-input" placeholder="Type reply..." /><button class="btn btn-primary">Send</button></div>
  </div>
</div>
"""
generate_page("recruiter/messages.html", "Recruiter", "Recruiter Chat", RECRUITER_NAV, "messages", "AM", "Alex Morrison", "Senior Recruiter", recruiter_messages)


# ----------------------------------------------------
# ADMIN PAGES DEFINITION
# ----------------------------------------------------
admin_users = """
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
  <h2>User Management</h2>
</div>
<div class="card">
  <table style="width:100%; border-collapse:collapse; text-align:left; font-size:13.5px;">
    <thead>
      <tr style="border-bottom:1px solid var(--border); color:var(--text-3);">
        <th style="padding:12px;">User</th>
        <th style="padding:12px;">Email</th>
        <th style="padding:12px;">Role</th>
        <th style="padding:12px;">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:12px; font-weight:600;">Priya Sharma</td>
        <td style="padding:12px;">priya@gmail.com</td>
        <td style="padding:12px;"><span class="badge badge-success" style="background:rgba(99,102,241,0.15); color:var(--primary-light);">Job Seeker</span></td>
        <td style="padding:12px;">Active</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:12px; font-weight:600;">TechCorp HR</td>
        <td style="padding:12px;">hr@techcorp.com</td>
        <td style="padding:12px;"><span class="badge badge-warning">Employer</span></td>
        <td style="padding:12px;">Active</td>
      </tr>
    </tbody>
  </table>
</div>
"""
generate_page("admin/users.html", "Administrator", "Users Management", ADMIN_NAV, "users", "SA", "Platform Admin", "System Controller", admin_users)

admin_jobs = """
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
  <h2>Jobs moderation</h2>
</div>
<div class="card">
  <table style="width:100%; border-collapse:collapse; text-align:left; font-size:13.5px;">
    <thead>
      <tr style="border-bottom:1px solid var(--border); color:var(--text-3);">
        <th style="padding:12px;">Job Details</th>
        <th style="padding:12px;">Company</th>
        <th style="padding:12px;">Flags</th>
        <th style="padding:12px;">Action</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:12px; font-weight:600;">Data Entry Associate</td>
        <td style="padding:12px;">Spam Company Ltd</td>
        <td style="padding:12px;"><span class="badge badge-error">5 Flags</span></td>
        <td style="padding:12px;"><button class="btn btn-secondary" style="padding:4px 8px; font-size:11px;" onclick="alert('Job removed!')">Take Down</button></td>
      </tr>
    </tbody>
  </table>
</div>
"""
generate_page("admin/jobs.html", "Administrator", "Jobs Moderation", ADMIN_NAV, "jobs", "SA", "Platform Admin", "System Controller", admin_jobs)

admin_reports = """
<div class="card">
  <h3 class="card-title">Platform Operations Audit Logs</h3>
  <div style="display:flex; flex-direction:column; gap:10px; margin-top:20px; font-size:13px;">
    <div style="border-bottom:1px solid var(--border); padding-bottom:8px;">[14:23:10] User <strong>Priya Sharma</strong> updated resume. <span style="color:var(--text-3);">IP: 192.168.1.42</span></div>
    <div style="border-bottom:1px solid var(--border); padding-bottom:8px;">[14:22:45] Employer <strong>TechCorp Inc</strong> posted new job role.</div>
  </div>
</div>
"""
generate_page("admin/reports.html", "Administrator", "Reports &amp; Logs", ADMIN_NAV, "reports", "SA", "Platform Admin", "System Controller", admin_reports)

admin_settings = """
<div class="card">
  <h3 class="card-title">System Settings</h3>
  <div class="form-grid">
    <div class="form-group"><label class="form-label">Platform Name</label><input type="text" class="form-input" value="TalentArc Platform" /></div>
    <div class="form-group"><label class="form-label">Global Mail Gateway</label><input type="text" class="form-input" value="smtp.sendgrid.net" /></div>
  </div>
</div>
"""
generate_page("admin/settings.html", "Administrator", "Platform Configuration", ADMIN_NAV, "settings", "SA", "Platform Admin", "System Controller", admin_settings)


# ----------------------------------------------------
# PUBLIC PAGES DEFINITION
# ----------------------------------------------------
public_job_details = """
<div style="max-width:800px; margin:40px auto; padding:0 20px;">
  <div class="card">
    <div style="display:flex; justify-content:space-between; align-items:flex-start;">
      <div style="display:flex; gap:16px; align-items:center;">
        <div class="profile-avatar" style="width:56px; height:56px; background:#4F46E5; border-radius:var(--r-md); font-weight:800; font-size:24px;">S</div>
        <div>
          <h2>Senior Software Engineer</h2>
          <p style="color:var(--text-2);">Stripe · San Francisco, CA · Remote Eligible</p>
        </div>
      </div>
      <a href="../seeker/apply.html" class="btn btn-primary">Apply Now</a>
    </div>
    <div style="display:flex; gap:16px; margin-top:20px; font-weight:700;">
      <span>Salary: $180K – $240K</span>
      <span style="color:var(--success);">Match Score: 96%</span>
    </div>
    <div style="border-top:1px solid var(--border); margin-top:24px; padding-top:24px; line-height:1.7;">
      <h3>About Stripe</h3>
      <p style="color:var(--text-2); margin-top:8px;">Stripe is a financial infrastructure platform for the internet. Millions of companies—from the world’s largest enterprises to the most ambitious startups—use Stripe to accept payments, grow their revenue, and accelerate new business opportunities.</p>
      
      <h3 style="margin-top:24px;">Requirements</h3>
      <ul style="list-style:disc; margin-left:20px; margin-top:8px; color:var(--text-2); display:flex; flex-direction:column; gap:8px;">
        <li>5+ years of experience with React, JavaScript/TypeScript, and modern web APIs</li>
        <li>Experience building highly reliable, distributed microservices in Go or Java</li>
        <li>Strong system design skills and commitment to developer experience</li>
      </ul>
    </div>
  </div>
</div>
"""
generate_page("public/job-details.html", "", "Job Details", None, "", "", "", "", public_job_details)

public_companies = """
<div style="max-width:1000px; margin:40px auto; padding:0 20px;">
  <h2>Browse Companies</h2>
  <p style="color:var(--text-3); margin-top:4px;">Explore 180K+ top tech organizations</p>
  <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:20px; margin-top:24px;">
    <div class="card">
      <div style="font-size:24px; font-weight:800; color:var(--primary-light);">Stripe</div>
      <p style="font-size:13px; color:var(--text-2); margin-top:8px;">Fintech infrastructure platform for internet payments.</p>
      <a href="job-details.html" class="btn btn-secondary" style="margin-top:16px; width:100%; justify-content:center;">View 48 Open Roles</a>
    </div>
    <div class="card">
      <div style="font-size:24px; font-weight:800; color:var(--accent);">Vercel</div>
      <p style="font-size:13px; color:var(--text-2); margin-top:8px;">The platform for frontend developers and Next.js.</p>
      <a href="job-details.html" class="btn btn-secondary" style="margin-top:16px; width:100%; justify-content:center;">View 23 Open Roles</a>
    </div>
  </div>
</div>
"""
generate_page("public/companies.html", "", "Explore Companies", None, "", "", "", "", public_companies)

public_resources = """
<div style="max-width:1000px; margin:40px auto; padding:0 20px;">
  <h2>Career Resources &amp; Guides</h2>
  <p style="color:var(--text-3);">Expert advice to level up your engineering career</p>
  <div style="display:grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap:20px; margin-top:24px;">
    <div class="card">
      <h4>How to Write an ATS-Friendly Resume</h4>
      <p style="font-size:12.5px; color:var(--text-2); margin-top:8px;">Learn the structural secrets that get your resume past initial bots and directly to engineers.</p>
      <a href="#" style="color:var(--primary-light); font-size:13px; margin-top:12px; display:inline-block;">Read Guide →</a>
    </div>
    <div class="card">
      <h4>Mastering System Design Interviewing</h4>
      <p style="font-size:12.5px; color:var(--text-2); margin-top:8px;">A step-by-step roadmap from scale metrics up to complete architectural definitions.</p>
      <a href="#" style="color:var(--primary-light); font-size:13px; margin-top:12px; display:inline-block;">Read Guide →</a>
    </div>
  </div>
</div>
"""
generate_page("public/resources.html", "", "Resources Center", None, "", "", "", "", public_resources)

print("All 21 pages generated successfully!")
