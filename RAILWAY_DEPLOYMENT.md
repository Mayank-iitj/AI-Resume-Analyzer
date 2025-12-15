# AI Resume Analyzer - Railway Deployment Guide

## 🚀 Quick Deploy to Railway

Railway.app is perfect for deploying Streamlit applications with minimal configuration.

### Prerequisites
- GitHub account
- Railway account (free at [railway.app](https://railway.app))
- Your code pushed to GitHub

---

## Deployment Steps

### 1. Push Your Code to GitHub

```bash
cd d:\AI-Resume-Analyzer
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

### 2. Deploy to Railway

1. Go to [railway.app](https://railway.app)
2. Click **"Start a New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your repository: `AI-Resume-Analyzer`
5. Railway will automatically detect the configuration from `railway.json`

### 3. Configure Environment Variables

In Railway dashboard:
1. Click on your deployed service
2. Go to **"Variables"** tab
3. Add the following environment variable:

```
DB_ENABLED=false
```

**Note**: Setting `DB_ENABLED=false` runs the app in demo mode (resume analysis works, but Admin/Feedback features are disabled). This is perfect for initial deployment.

### 4. Wait for Deployment

Railway will:
- Install dependencies from `requirements.txt`
- Download spaCy model
- Run setup script
- Start your Streamlit app

Deployment typically takes 3-5 minutes.

### 5. Access Your App

Once deployed, Railway provides a public URL like:
```
https://your-app-name.up.railway.app
```

---

## Optional: Enable Database Features

To enable Admin panel and Feedback storage, you need a database.

### Option A: Use Railway PostgreSQL (Recommended)

1. In Railway dashboard, click **"+ New"** → **"Database"** → **"Add PostgreSQL"**
2. Railway will create a database and set environment variables automatically
3. Update your app's environment variables:

```bash
DB_ENABLED=true
DB_HOST=${{PGHOST}}
DB_USER=${{PGUSER}}
DB_PASSWORD=${{PGPASSWORD}}
DB_NAME=${{PGDATABASE}}
DB_PORT=${{PGPORT}}
```

**Note**: You'll need to modify `App.py` to support PostgreSQL (currently uses MySQL/PyMySQL).

### Option B: Use External MySQL Database

Services like [PlanetScale](https://planetscale.com/) or [Railway MySQL](https://railway.app/):

1. Create a MySQL database
2. Get connection credentials
3. Add to Railway environment variables:

```bash
DB_ENABLED=true
DB_HOST=your-mysql-host.railway.app
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=cv
DB_PORT=3306
```

---

## Configuration Files Explained

### `Procfile`
Tells Railway how to start your app:
```
web: sh setup.sh && streamlit run App/App.py --server.port=$PORT --server.address=0.0.0.0
```

### `railway.json`
Railway-specific configuration:
- Build command: Install dependencies and spaCy model
- Start command: Run setup and start Streamlit
- Restart policy: Automatically restart on failure

### `requirements.txt`
Python dependencies - already configured for Python 3.13 compatibility

### `setup.sh`
Setup script that:
- Creates necessary directories
- Downloads NLTK data
- Downloads spaCy language model

---

## Environment Variables Reference

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DB_ENABLED` | No | `false` | Enable database features |
| `DB_HOST` | If DB enabled | `localhost` | Database host |
| `DB_USER` | If DB enabled | `root` | Database username |
| `DB_PASSWORD` | If DB enabled | - | Database password |
| `DB_NAME` | If DB enabled | `cv` | Database name |
| `DB_PORT` | If DB enabled | `3306` | Database port |
| `PORT` | No | Auto-set by Railway | App port |

---

## Features in Demo Mode (DB_ENABLED=false)

✅ **Available:**
- Resume upload and parsing
- Skills extraction
- Career field prediction
- Experience level detection
- Resume scoring
- Course recommendations
- Video recommendations

❌ **Disabled:**
- Admin panel
- Feedback submission
- User analytics
- Data storage

---

## Troubleshooting

### Build Fails

**Check logs** in Railway dashboard for specific errors.

Common issues:
- **spaCy model download fails**: Railway will retry automatically
- **NLTK data missing**: Ensure `setup.sh` runs successfully
- **Dependency conflicts**: Check `requirements.txt` versions

### App Crashes on Startup

1. Check Railway logs for error messages
2. Verify environment variables are set correctly
3. Ensure `DB_ENABLED=false` if no database configured

### Geocoding Errors

The app includes fallback handling for geocoding failures. If geocoding service is unavailable, it will use default values without crashing.

### File Upload Issues

Railway provides ephemeral storage. Uploaded files are stored temporarily and will be deleted when the container restarts. This is normal behavior for cloud deployments.

---

## Updating Your Deployment

After making code changes:

```bash
git add .
git commit -m "Your update message"
git push origin main
```

Railway will automatically detect the changes and redeploy.

---

## Cost

Railway offers:
- **Free tier**: $5 credit per month (usually enough for small apps)
- **Hobby plan**: $5/month for more resources
- **Pro plan**: Pay-as-you-go for production apps

Your Streamlit app should run comfortably on the free tier for testing and small-scale use.

---

## Alternative: Local Testing Before Deployment

Test Railway configuration locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run setup
sh setup.sh

# Set environment variable
set DB_ENABLED=false  # Windows
export DB_ENABLED=false  # Linux/Mac

# Run app
streamlit run App/App.py --server.port=8501 --server.address=0.0.0.0
```

---

## Next Steps

1. ✅ Deploy to Railway with `DB_ENABLED=false`
2. ✅ Test resume analysis features
3. 📊 (Optional) Add database for Admin/Feedback features
4. 🎨 (Optional) Customize branding and content
5. 🔒 (Optional) Add custom domain

---

## Support

- **Railway Docs**: [docs.railway.app](https://docs.railway.app)
- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **Project Issues**: Create an issue on your GitHub repository

---

## Security Notes

⚠️ **Important**:
- Never commit `.env` file to Git (already in `.gitignore`)
- Change default admin credentials in production
- Use strong database passwords
- Enable HTTPS (Railway provides this automatically)

---

**Happy Deploying! 🚀**
