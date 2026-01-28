# ContentFlow: Click-by-Click Deployment Guide

Follow these steps exactly to get your automated SaaS running.

---

## Part 1: Supabase Setup (The Database)

1.  **Login**: Go to [database.new](https://database.new) (Supabase).
2.  **Create Project**:
    *   Click **"New Project"**.
    *   **Name**: `Mula-ContentFlow`
    *   **Password**: Create one and **SAVE IT**.
    *   **Region**: Pick the one closest to you.
    *   Wait ~2 minutes for it to "provision".
3.  **Run the SQL code**:
    *   On the left sidebar, click the **"SQL Editor"** icon (looks like `>_`).
    *   Click **"+ New Query"**.
    *   Paste this exact code:
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
    *   Click the **"Run"** button at the bottom right. You should see "Success".
4.  **Get your Keys**:
    *   On the left sidebar, click the **"Settings"** icon (gear ⚙️).
    *   Click **"API"**.
    *   Copy the **Project URL** (starts with `https://`).
    *   Copy the **anon public key** (starts with `eyJ...`).

---

## Part 2: Render Setup (The Brain)

1.  **Login**: Go to [dashboard.render.com](https://dashboard.render.com).
2.  **Create Service**:
    *   Click the blue **"New +"** button -> Select **"Web Service"**.
    *   Select **"Build and deploy from a Git repository"**.
    *   Click on your `Mula-ContentFlow` repo.
3.  **Basic Configuration**:
    *   **Name**: `mula-backend`
    *   **Root Directory**: `agents`
    *   **Runtime**: `Docker`
    *   **Instance Type**: `Free`
4.  **How to add Secrets (The "Environment" Step)**:
    *   Scroll all the way to the bottom of the page.
    *   Look for a button that says **"Advanced"** OR look at the sidebar on the left if you already finished creating it.
    *   **IF YOU ARE ON THE CREATION PAGE**:
        *   Scroll down and click **"Advanced"**.
        *   Click **"Add Environment Variable"**.
    *   **IF YOU ALREADY CREATED THE SERVICE**:
        *   Click on your service name (`mula-backend`) in the dashboard.
        *   On the left sidebar, click **"Environment"**.
        *   Click **"Add Environment Variable"**.
5.  **Enter These 3 Variables**:
    
    | Key | Value |
    | :--- | :--- |
    | `OPENAI_API_KEY` | `sk-proj-...` (Your OpenAI Key) |
    | `SUPABASE_URL` | `https://ciawpsxbbfnrhiydytpk.supabase.co` |
    | `SUPABASE_KEY` | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` (The long key) |
    
6.  **Finalize**: Scroll down and click **"Create Web Service"** (or "Save Changes" if you already created it).
7.  **Wait**: Render will now build your app. Once it says **"Live"** in green, your backend is ready.
8.  **Get the URL**: Your URL is: `https://mula-backendmula-backendmula-contentflow.onrender.com`


---

## Part 3: Vercel Setup (The Website)

1.  **Open Vercel**: Go to your project on [vercel.com](https://vercel.com).
2.  **Settings**:
    *   Click **"Settings"** -> **"Environment Variables"**.
    *   Add/Update `NEXT_PUBLIC_API_URL`.
    *   **Value**: Paste the Render URL from Part 2.
3.  **Redeploy**:
    *   Go to the **"Deployments"** tab.
    *   Click the three dots `...` on the latest deployment.
    *   Select **"Redeploy"**.

---

**You are now live!** Open your Vercel URL and try it out.
