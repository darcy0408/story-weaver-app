# Claude Handoff Document - 2025-11-10 Evening
**Created:** 2025-11-10, 9:30 PM
**Token Usage:** 137k/200k (69%)
**Branch:** main
**Status:** Ready to start 21-day launch plan

---

## 🎯 CURRENT STATUS

### ✅ What We Just Completed
1. **Created comprehensive 21-day launch plan** - `21_DAY_MASTER_PLAN.md`
2. **Analyzed Gemini & Codex recommendations** - `AI_RECOMMENDATIONS_ANALYSIS.md`
3. **Created detailed task lists:**
   - `CODEX_TASKS_21_DAY.md` - 10 tasks, 8 work days
   - `GEMINI_TASKS_21_DAY.md` - 8 tasks, 7 work days
4. **Centralized backend URLs** - All API calls now use `Environment.backendUrl`
5. **Cleaned up git** - Everything committed and pushed to main

### 🚨 CRITICAL ISSUE - Not Yet Resolved
**Story generation returns one-sentence fallback story**

**Root Cause:** Railway API key issue (multiple projects confusion)
- Have 3 Railway projects: `selfless-renewal`, `radiant-tranquility`, and one other
- `selfless-renewal` doesn't have Gemini API key configured
- Need to consolidate to single project with proper API key

**Status:** Gemini is working on fixing this right now

**User said:** Interactive stories work fine, regular stories return fallback

---

## 🚫 IMPORTANT: Do NOT Do This

### google-genai Package Switch
**Gemini wants to switch from `google-generativeai` to `google-genai`**

**DO NOT LET THEM!** Here's why:
1. **Same cost** - Both call same API, no pricing difference
2. **Breaking change** - Different imports, different syntax
3. **Not the problem** - Won't fix story generation
4. **More work** - Have to update all Gemini calls
5. **Risk** - Could break working code before launch

**If Gemini pushes on this, say:**
> "We're sticking with google-generativeai for now. It's not the package - it's the Railway API key configuration. Test after that's fixed."

**User has these uncommitted changes sitting (DO NOT COMMIT):**
```bash
backend/requirements.txt - google-generativeai => google-genai
backend/app.py - import changes
```

**Tell user to revert:**
```bash
git restore backend/requirements.txt
git restore backend/app.py
```

---

## 📋 The 21-Day Plan Overview

### Week 1 (Days 1-7): Critical Infrastructure
**Goal:** Make it work at scale, protect revenue

| Day | Who | Task | Priority |
|-----|-----|------|----------|
| 1 | Claude | PostgreSQL + Centralize URLs | CRITICAL |
| 1 | Gemini | PostgreSQL migration script | CRITICAL |
| 2 | Claude | Async task queue (Celery + Redis) | CRITICAL |
| 3-4 | Claude | Backend tests (Pytest) | CRITICAL |
| 3-4 | Codex | Frontend tests (Flutter) | CRITICAL |
| 5 | Claude | Secure storage (flutter_secure_storage) | CRITICAL |
| 6 | Claude | Crash reporting (Sentry) | HIGH |
| 7 | Claude | Start real billing (IAP setup) | CRITICAL |

### Week 2 (Days 8-14): Architecture + Revenue
**Goal:** Clean code, real payments, beta testing

| Day | Who | Task | Priority |
|-----|-----|------|----------|
| 8 | Claude | Complete billing integration | CRITICAL |
| 9 | Codex | Backend resilience (retry logic) | HIGH |
| 10-11 | Claude | State management (Riverpod) | HIGH |
| 12-13 | Gemini | Backend modularization | HIGH |
| 14 | Gemini | User accounts + server sync | HIGH |
| 14 | All | **Beta release** to 5-10 testers | CRITICAL |

### Week 3 (Days 15-21): Polish + Launch
**Goal:** Professional UX, final testing, launch

| Day | Who | Task | Priority |
|-----|-----|------|----------|
| 15 | Codex | Build flavors | MEDIUM |
| 16 | Codex | Offline mode (Isar) | HIGH |
| 17 | Codex | UX polish + onboarding | HIGH |
| 18 | Codex | Analytics (Firebase) | HIGH |
| 19 | Codex | User documentation | HIGH |
| 20 | Codex | Final QA & bug bash | CRITICAL |
| 21 | Claude | **Production launch** | CRITICAL |

---

## 📁 Key Files to Know

### Planning Documents (Read These First!)
- `21_DAY_MASTER_PLAN.md` - Complete day-by-day roadmap
- `AI_RECOMMENDATIONS_ANALYSIS.md` - Gemini vs Codex comparison
- `CODEX_TASKS_21_DAY.md` - Codex's specific tasks with code examples
- `GEMINI_TASKS_21_DAY.md` - Gemini's specific tasks with code examples
- `13_DAY_MASTER_DEPLOYMENT_PLAN.md` - Original plan (superseded by 21-day)
- `GEMINI_AUDIT_RESPONSE.md` - My assessment of Gemini's recommendations

### AI Audit Documents
- `required improvements.md` - Gemini's 10 recommendations (architecture focus)
- `codex_improvements.md` - Codex's 10 recommendations (production focus)
- `GEMINI.md` - Gemini's notes

### Current Code Structure
```
story-weaver-app/
  backend/
    app.py - MONOLITHIC (1000+ lines) - Needs refactoring Day 12-13
    requirements.txt - Python dependencies
    characters.db - SQLite (migrate to PostgreSQL Day 1)
  lib/
    main_story.dart - Main UI (600+ lines) - Needs Riverpod Days 10-11
    character_creation_screen_enhanced.dart - Character form
    pre_story_feelings_dialog.dart - Feelings wheel dialog
    feelings_wheel_screen.dart - 72-emotion wheel
    services/
      api_service_manager.dart - API calls
      story_complexity_service.dart - Age-appropriate content
    config/
      environment.dart - Backend URL configuration
```

---

## 🔧 What Needs to Happen Next

### Immediate (Tonight/Tomorrow Morning):
1. **Fix Railway API Key Issue**
   - Gemini is working on this
   - Once fixed, test: does story generation work?
   - If yes: Start Day 1 tasks
   - If no: Debug the actual error (check Railway logs)

2. **Clean Up Old Branches**
   ```bash
   # These are already merged, safe to delete:
   git branch -d codex-dev
   git branch -d codex_in_charge
   git branch -d fix-network-error
   git branch -d gemini-deploy
   git branch -d gemini/feelings-wheel-ui
   git branch -d gemini/simplify-form
   ```

3. **Verify story_result_screen.dart Changes**
   ```bash
   git diff lib/story_result_screen.dart
   # Check if real changes or just line endings
   # If real, commit them
   # If line endings, restore them
   ```

### Day 1 Tasks (When Railway is Fixed):
**Morning: PostgreSQL Migration** (Claude + Gemini in parallel)
- Claude: Provision PostgreSQL on Railway
- Claude: Update `backend/app.py` connection string
- Gemini: Create migration script from SQLite
- Claude: Test character CRUD with PostgreSQL

**Afternoon: Centralize URLs** (Already done! ✅)
- ✅ All `http://127.0.0.1:5000` replaced with `Environment.backendUrl`
- ✅ Committed and pushed
- Just need to verify everything works

---

## 🎯 Success Criteria for Day 1

By end of Day 1, must have:
- ✅ PostgreSQL provisioned on Railway
- ✅ All existing characters migrated
- ✅ Backend using PostgreSQL (not SQLite)
- ✅ All API endpoints tested and working
- ✅ All frontend URLs centralized
- ✅ No hardcoded `http://127.0.0.1:5000` anywhere

---

## 🚨 Known Issues & Blockers

### 1. Railway API Key (BLOCKING)
**Status:** Gemini working on it
**Impact:** Story generation fails
**Fix:** Consolidate to one Railway project with proper key

### 2. One Uncommitted File
**File:** `lib/story_result_screen.dart`
**Status:** Modified but not committed
**Action:** Check diff, commit if real changes

### 3. Old Branches Cluttering Repo
**Count:** 6 merged branches still local
**Action:** Delete them (safe, already merged)

---

## 💬 Communication with Other AIs

### Tell Gemini:
1. **Priority:** Fix Railway API key first, then start Day 1 (PostgreSQL migration script)
2. **Do not:** Switch to google-genai package
3. **Branch:** Use `gemini/postgres-migration` for Day 1 task

### Tell Codex:
1. **Wait:** Not starting until Day 3 (frontend tests)
2. **Prepare:** Read `CODEX_TASKS_21_DAY.md` to understand your tasks
3. **Branch:** Will use `codex/frontend-tests` when starting

---

## 📊 Git Status Summary

**Current Branch:** main
**Remote:** origin/main (up to date)
**Uncommitted:** 1 file (`lib/story_result_screen.dart`)
**Untracked:** None (all docs committed)
**Old Branches:** 6 (safe to delete, already merged)

**Recent Commits:**
```
51c476b [Fix] Centralize all backend URLs
08edecb [Docs] Create detailed task lists for Codex and Gemini
a6c1474 [Docs] Create comprehensive 21-day launch plan
```

---

## 🔑 Key Decisions Made

### Architecture:
1. ✅ PostgreSQL over SQLite (Day 1)
2. ✅ Async task queue with Celery + Redis (Day 2)
3. ✅ Riverpod for state management (Days 10-11)
4. ✅ Backend modularization: models/routes/services (Days 12-13)

### Revenue & Security:
1. ✅ Real IAP billing required (Days 7-8)
2. ✅ flutter_secure_storage for API keys (Day 5)
3. ✅ Sentry for crash reporting (Day 6)
4. ✅ User accounts + JWT auth (Day 14)

### Timeline:
1. ✅ 21 days chosen over 13 days
2. ✅ Beta testing on Day 14
3. ✅ Production launch on Day 21
4. ✅ Parallel work streams (Codex frontend, Gemini backend)

---

## 🆘 If Something Goes Wrong

### Story Generation Fails After Railway Fix:
1. Check Railway logs: https://railway.app
2. Look for `!!! API ERROR:` lines (we added enhanced logging)
3. Check: prompt length, mode flags, character age
4. Verify Gemini API key is set correctly

### Can't Merge a Branch:
1. Check what's different: `git diff main branch-name`
2. Usually safe to take "theirs": `git checkout --theirs file.py`
3. If complex conflicts, create new handoff doc and ask user

### Accidentally Committed google-genai Change:
1. Revert last commit: `git revert HEAD`
2. Or reset to before: `git reset --hard HEAD~1`
3. Restore correct version: `git checkout origin/main -- backend/`

---

## 📝 Quick Commands Reference

### Start Day 1:
```bash
git checkout main
git pull origin main
# Claude works on PostgreSQL provisioning
# Gemini creates migration script on gemini/postgres-migration
```

### Check Railway Status:
```bash
curl https://story-weaver-app-production.up.railway.app/health
# Should return: {"status":"ok","has_api_key":true}
```

### Test Story Generation:
```bash
curl -X POST https://story-weaver-app-production.up.railway.app/generate-story \
  -H "Content-Type: application/json" \
  -d '{"character":"Test","theme":"Adventure","character_age":7}'
```

### Clean Up Old Branches:
```bash
git branch -d codex-dev codex_in_charge fix-network-error gemini-deploy gemini/feelings-wheel-ui gemini/simplify-form
```

---

## 🎯 What to Tell the User

**"We're ready to start the 21-day launch plan once Railway API key is fixed!"**

**Progress:**
- ✅ All planning documents created
- ✅ Task lists for Codex & Gemini ready
- ✅ Backend URLs centralized
- ✅ Git cleaned up
- ⏳ Waiting on Railway API key fix

**Next Steps:**
1. Gemini fixes Railway → test stories
2. If working → Start Day 1 (PostgreSQL)
3. If not → Debug actual error
4. Then follow 21-day plan to launch!

---

## 📚 Resources

**Railway Dashboard:** https://railway.app
**Netlify Dashboard:** https://app.netlify.com
**GitHub Repo:** https://github.com/darcy0408/story-weaver-app
**Production Frontend:** https://reliable-sherbet-2352c4.netlify.app
**Production Backend:** https://story-weaver-app-production.up.railway.app

**Gemini API Docs:** https://ai.google.dev/docs
**Flutter Docs:** https://docs.flutter.dev
**Railway Docs:** https://docs.railway.app

---

**Last Updated:** 2025-11-10, 9:30 PM
**Next Session:** Start Day 1 after Railway fix
**Priority:** Fix story generation, then PostgreSQL migration

🚀 **We're ready to launch in 21 days!**
