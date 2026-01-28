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

## 4. Supabase Setup
1. Create a table named `jobs`:
```sql
create table jobs (
  id uuid default gen_random_uuid() primary key,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null,
  video_url text not null,
  title text,
  format_type text,
  content text,
  status text
);
```
2. Add `SUPABASE_URL` and `SUPABASE_KEY` (Service Role Key or Anon Key with RLS disabled for MVP) to Render environment variables.

