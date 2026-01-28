# Deployment Instructions

## 1. Frontend (Vercel)
1.  Run `npx vercel` in `/web`.
2.  Login with your GitHub/Email.
3.  Add the Environment Variables from `.env.local` to Vercel Settings.

## 2. Backend (Render / Fly.io)
1.  You have a `Dockerfile` in `/agents`.
2.  Push this repo to GitHub.
    *   **Note**: If you signed in with Google, you need a **Personal Access Token** (PAT) instead of a password.
    *   Go to **GitHub Settings** -> **Developer Settings** -> **Personal Access Tokens (Tokens (classic))**.
    *   Generate a new token with `repo` scope.
    *   Use this token as your **Password** when pushing.
3.  Connect Render/Fly to the repo and point it to the `agents` folder.
4.  Add `OPENAI_API_KEY` to the environment variables on the dashboard.

## 3. Stripe
1.  Get your API Keys from [dashboard.stripe.com](https://dashboard.stripe.com).
2.  Add them to the Vercel variables.
