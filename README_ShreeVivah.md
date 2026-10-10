<!--
╔══════════════════════════════════════════════════════════════════════╗
║  ShreeVivah Matrimony — crafted with care by Simu (Srimanta Bag)    ║
║  Keep this README honest: document implemented features accurately.  ║
╚══════════════════════════════════════════════════════════════════════╝
-->

<div align="center">

  <img src="https://readme-typing-svg.demolab.com?font=Playfair+Display&weight=700&size=34&pause=1200&color=C084FC&center=true&vCenter=true&width=760&lines=ShreeVivah+Matrimony;Where+Meaningful+Connections+Begin;Thoughtfully+Built+with+Django" alt="Animated ShreeVivah title" />

  <p><strong>A thoughtful digital space for discovering profiles and celebrating meaningful connections.</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+" />
    <img src="https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django 5.2" />
    <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML CSS JavaScript" />
    <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  </p>

  <p>
    <img src="https://img.shields.io/badge/Status-Active%20Development-8B5CF6?style=flat-square" alt="Active development" />
    <img src="https://img.shields.io/badge/Author-Simu%20%7C%20Srimanta%20Bag-DB2777?style=flat-square" alt="Author Simu Srimanta Bag" />
    <img src="https://img.shields.io/badge/License-Not%20Specified-64748B?style=flat-square" alt="License not specified" />
  </p>

  <p><em>Built with care by Simu • Srimanta Bag</em></p>

</div>

---

## ✨ About ShreeVivah

**ShreeVivah Matrimony** is a Django-powered matrimony website designed to help visitors discover Bride and Groom profiles, search by name, create member-submitted profiles, explore wedding-related pages, and manage selected content through Django Admin.

The project combines a profile-discovery experience with wedding and ceremony content in a responsive website built with Django templates, HTML, CSS, and vanilla JavaScript.

> **Project transparency:** This README documents the implementation currently present in the repository. Some pages are informational or browser-side demonstrations. Contact submissions, membership checkout, and some Hand-page interactions do not currently have complete server-side persistence or payment processing.

## 🧭 Contents

- [Highlights](#-highlights)
- [Technology stack](#-technology-stack)
- [Project architecture](#-project-architecture)
- [Getting started](#-getting-started)
- [Run locally](#-run-locally)
- [Application routes](#-application-routes)
- [Accounts and permissions](#-accounts-and-permissions)
- [Profiles and uploads](#-profiles-and-uploads)
- [Admin content management](#-admin-content-management)
- [Checks and tests](#-checks-and-tests)
- [Current limitations](#-current-limitations)
- [Roadmap](#-roadmap)
- [Production readiness](#-production-readiness)
- [Author](#-author)

## 🌟 Highlights

<table>
  <tr>
    <td width="50%">
      <h3>💞 Profile discovery</h3>
      Browse separate Bride and Groom directories, view profile details, and search for profiles by name.
    </td>
    <td width="50%">
      <h3>🔐 Member accounts</h3>
      Sign up, sign in, sign out, and access member-protected pages through Django authentication.
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>🖼️ Profile submissions</h3>
      Signed-in members can submit Bride or Groom profiles and optionally include a photo.
    </td>
    <td width="50%">
      <h3>🛠️ Django Admin</h3>
      Manage curated profiles, Firstlove stories, Mehendi categories and designs, users, groups, and permissions.
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>💍 Wedding experiences</h3>
      Explore About, Services, Wedding Gallery, Membership Plans, Haldi, Mehendi, Together, and other wedding-related pages.
    </td>
    <td width="50%">
      <h3>📱 Responsive interface</h3>
      Responsive page layouts, selected gallery dialogs/lightboxes, and browser-local tools on the Hand page.
    </td>
  </tr>
</table>

### More implemented functionality

- Profile-name suggestions and search result handling.
- Curated sample profiles with featured-profile ordering.
- Success Stories gallery with twelve template-defined cards and a photo/details dialog.
- Member submissions for Firstlove stories and Mehendi designs.
- Comment forms on the comment pages.
- Optional profile and gallery image uploads.

## 🧰 Technology stack

| Layer | Tools |
|---|---|
| Backend | Python, Django 5.2 |
| Frontend | Django Templates, HTML5, CSS3, vanilla JavaScript |
| Local database | SQLite |
| Image processing/uploads | Pillow |
| Authentication | Django authentication system |
| Content administration | Django Admin |
| Static assets | Django static files, CSS, JavaScript, images, and video |

**Runtime dependencies:** The repository currently does not include a `requirements.txt`, `pyproject.toml`, or `package.json`. The documented Python runtime dependencies are Django and Pillow.

## 🏗️ Project architecture

```text
StrongBond/
├── accounts/                 # Signup, login, logout, account templates/assets
├── main/                     # Homepage, Bride/Groom, comments, contact, stories
│   ├── migrations/           # Database and profile-data migrations
│   ├── static/main/          # Main app CSS, JavaScript, images
│   └── templates/main/       # Main app templates
├── matrimony_site/           # Settings, root URLs, WSGI and ASGI
├── profiles/                 # Profile search, suggestions, detail pages
├── works/                    # Wedding pages and content models
│   ├── migrations/
│   ├── static/works/         # CSS, JavaScript, images, videos
│   └── templates/works/
├── static/                   # Shared static assets
├── media/                    # User-uploaded files (runtime)
├── db.sqlite3                # Local SQLite database
└── manage.py                 # Django management entry point
```

The installed Django apps are `main`, `accounts`, `works`, and `profiles`. The `matrimony_site` package contains the project configuration.

## 🚀 Getting started

### Prerequisites

- Python **3.10 or later** (Python 3.13 has been used with this project).
- `pip`.
- A modern web browser.
- Internet access for external Google Fonts and Font Awesome stylesheets used by some pages.

### 1. Open the project folder

Open PowerShell in the directory that contains `manage.py`.

```powershell
cd path\to\StrongBond
```

Replace `path\to\StrongBond` with your actual project path.

### 2. Create and activate a virtual environment

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use the Python executable directly from `.venv\Scripts\python.exe`, or review your local PowerShell execution policy before changing it.

### 3. Install dependencies

```powershell
python -m pip install Django==5.2.5 Pillow==11.3.0
```

### 4. Apply database migrations

```powershell
python manage.py migrate
```

Migrations create/update the local schema and include migrations for the curated sample Bride/Groom profile data.

### 5. Create an administrator account

```powershell
python manage.py createsuperuser
```

Follow the prompts to set the admin username, email (if requested), and password.

### 6. Start the development server

```powershell
python manage.py runserver
```

Open these addresses in your browser:

| Service | URL |
|---|---|
| Website | http://127.0.0.1:8000/ |
| Django Admin | http://127.0.0.1:8000/admin/ |

### macOS / Linux activation

```bash
source .venv/bin/activate
```

The remaining `python manage.py ...` commands are the same.

## 🗺️ Application routes

Routes marked **Member** require sign-in. The admin route requires an active staff account and the relevant permissions.

| Route | Purpose | Access |
|---|---|---|
| `/` | Homepage | Public |
| `/accounts/signup/` | Create an account | Public |
| `/accounts/login/` | Sign in | Public |
| `/accounts/logout/` | Sign out | Public |
| `/search/?q=NAME` | Search profiles | Public |
| `/profiles/search/?q=NAME` | Profile search results | Public |
| `/profiles/search/suggestions/?q=NAME` | JSON profile-name suggestions | Public |
| `/profiles/details/<slug>/` | Curated profile details | Public |
| `/profiles/rahul/`, `/profiles/brent/`, etc. | Named curated profile pages | Public |
| `/success_stories/` | Success Stories gallery | Member |
| `/about/` | About page | Member |
| `/contact/` | Contact page | Member |
| `/bride/`, `/groom/` | Bride/Groom directories | Member |
| `/bride/<id>/`, `/groom/<id>/` | Profile details | Member |
| `/create-bride/`, `/create-groom/` | Submit a profile | Member |
| `/comments/`, `/comments1/` | Comment pages | Member |
| `/works/work/` | Wedding Gallery | Member |
| `/works/services/` | Services | Member |
| `/works/plans/` | Membership Plans information | Member |
| `/works/firstlook/` | Firstlove stories and form | Member |
| `/works/mehendi/` | Mehendi gallery and form | Member |
| `/works/haldi/` | Haldi page | Member |
| `/works/fire/` | Fire ceremony page | Member |
| `/works/together/` | Together page | Member |
| `/works/hand/` | Hand page and browser-side tools | Member |
| `/admin/` | Django administration | Staff with permissions |

> Both `/search/` and `/profiles/search/` are registered routes for profile searching.

## 🔐 Accounts and permissions

### Visitors
- Can access the homepage, signup, login, profile search, search suggestions, and curated static profile routes.
- Must sign in to access member-protected pages and submit content.

### Signed-in members
- Can browse protected profile directories, wedding pages, and other member-only pages.
- Can submit Bride/Groom profiles with optional photos.
- Can submit Firstlove stories and Mehendi designs.
- Can post text through the comment forms.

### Staff and administrators
- Django Admin uses Django's built-in staff access and model-permission checks.
- Superusers can manage registered models.
- Staff access depends on assigned model permissions.
- Bride and Groom sample profiles are maintained in separate admin sections.

**Current boundary:** The project does not define custom role groups or custom per-record admin permissions. The public interface also does not yet provide a complete member profile edit/delete workflow or ownership-based profile dashboard.

## 🖼️ Profiles and uploads

Bride and Groom records are stored separately:

- `main.BrideProfile`
- `main.GroomProfile`

Profiles support details such as name, slug, profession, location, about text, expectations, family details, photo/image path, and sample/featured flags.

- Sample profiles have no member owner and use `is_sample=True`.
- Member-submitted profiles are associated with the submitting user.
- `is_featured` controls featured sample ordering/presentation.
- Uploaded profile photos are stored under `media/bride_photos/` or `media/groom_photos/`.
- Curated static images remain in app static assets.

Keep user uploads in `media/`, not in static asset directories.

## 🛠️ Admin content management

Sign in at `/admin/` with a superuser or a staff account with the required permissions.

| Admin section | Manages |
|---|---|
| Bride profiles | Bride profile details, sample/featured flags, photos and image paths |
| Groom profiles | Groom profile details, sample/featured flags, photos and image paths |
| Firstlove stories | Story title, description, uploaded image or static image path |
| Mehendi types | Categories/styles used to classify designs |
| Mehendi designs | Title, category, description, image, submitter, creation time |
| Users / Groups / Permissions | Django accounts and access permissions |

To add a curated profile, choose the correct Bride or Groom section, enter the profile details, and configure its sample/featured status and image. Keep Bride and Groom records in their respective sections.

## 🧪 Checks and tests

Run Django's configuration check:

```powershell
python manage.py check
```

Run the full test suite:

```powershell
python manage.py test
```

Run individual app tests:

```powershell
python manage.py test accounts
python manage.py test main
python manage.py test profiles
python manage.py test works
```

Other useful commands:

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

Use `makemigrations` after model changes. `collectstatic` gathers static assets for production and is not normally required for local development.

The existing tests cover authentication, profile flows and administration, search, Success Stories rendering/dialog support, Firstlove and Mehendi submissions, and related page behavior.

## ⚠️ Current limitations

The following features are **not yet complete production workflows**:

- **Contact form:** The page renders a form, but the current view does not validate/save submissions, send email, or provide a complete confirmation workflow.
- **Membership plans:** Plan information is displayed, but payment processing, subscription lifecycle, and entitlement enforcement are not wired up.
- **Success Stories:** The twelve displayed cards are hard-coded in the template; they do not have a dedicated model/admin workflow.
- **Hand page:** Some values use browser `localStorage`; other selections are temporary UI state and are not shared with the server or other devices.
- **Member profile maintenance:** Members can create profiles, but self-service edit/delete and an ownership-based dashboard are not complete.
- **Privacy and moderation:** A custom profile visibility workflow, approval queue, and record-level privacy policy are not implemented.
- **Comments:** Comment forms store text, but a moderation/approval workflow is not configured.
- **Production services:** Production email, cloud media storage, and deployment configuration are not included.

## 🧭 Roadmap

Potential next steps for the project:

- [ ] Implement and test Contact submissions, validation, and email delivery.
- [ ] Add member-owned profile dashboards with edit/delete permissions.
- [ ] Add profile review, visibility, privacy, and moderation controls.
- [ ] Move Success Stories into database-backed models and Django Admin.
- [ ] Add comment moderation and reporting.
- [ ] Integrate a payment provider and subscription lifecycle before advertising paid plans as functional.
- [ ] Configure production email and persistent/private media storage.
- [ ] Add automated tests for authorization, privacy, uploads, and important user journeys.
- [ ] Configure deployment, static-file hosting, monitoring, and database backups.

## 🚢 Production readiness

The checked-in Django configuration is for local development. Before deploying to production:

1. Move `SECRET_KEY` to a private environment variable and rotate it if a real deployment has exposed the checked-in value.
2. Set `DEBUG=False` and configure `ALLOWED_HOSTS` for the deployed domains.
3. Configure HTTPS, secure session/CSRF cookies, trusted origins, and Django deployment security settings.
4. Use a production database and test your backup/restore process.
5. Configure a production static-file server and persistent/private media storage with suitable upload access controls.
6. Configure a production email backend if the site needs to send account or contact messages.
7. Review authentication redirects, logout/CSRF behavior, staff permissions, profile privacy, and moderation.
8. Run migrations, `collectstatic`, `python manage.py check --deploy`, and the full test suite as part of deployment.
9. Keep credentials, secret keys, private uploads, and production database files out of source control.

For local development, SQLite is suitable. For a public production deployment, choose and configure a database and file-storage strategy appropriate to your hosting environment.

## 👨‍💻 Author

<div align="center">

  <h3>Simu — Srimanta Bag</h3>
  <p><strong>Developer • Tech Explorer • Entrepreneurial Mindset</strong></p>
  <p><em>Building thoughtful digital experiences, one project at a time.</em></p>

  <!-- Replace these URLs if your public profile links change. -->
  <a href="https://github.com/DeveloperSimu">
    <img src="https://img.shields.io/badge/GitHub-DeveloperSimu-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub DeveloperSimu" />
  </a>

  <p>Designed and developed with care by <strong>Simu (Srimanta Bag)</strong>.</p>

</div>

---

<div align="center">
  <sub>ShreeVivah Matrimony · Thoughtful connections, thoughtfully built.</sub>
</div>
