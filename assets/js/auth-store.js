// assets/js/auth-store.js
const TA_USERS_KEY = 'ta_users';
const TA_SESSION_KEY = 'ta_session';

function taGetUsers() {
  return JSON.parse(localStorage.getItem(TA_USERS_KEY) || '{}');
}
function taSaveUsers(users) {
  localStorage.setItem(TA_USERS_KEY, JSON.stringify(users));
}

function taRegisterUser({ firstName, lastName, email, password, role }) {
  const users = taGetUsers();
  const key = email.trim().toLowerCase();
  if (users[key]) return { ok: false, error: 'An account with this email already exists.' };

  users[key] = {
    email: key,
    password,
    firstName,
    lastName,
    role: role || 'seeker',
    profile: {
      fullName: `${firstName} ${lastName}`.trim(),
      email: key,
      phone: '',
      location: '',
      about: '',
      resume: null
    }
  };
  taSaveUsers(users);
  localStorage.setItem(TA_SESSION_KEY, key);
  return { ok: true, user: users[key] };
}

function taLoginUser(email, password) {
  const users = taGetUsers();
  const key = email.trim().toLowerCase();
  const user = users[key];
  if (!user || user.password !== password) {
    return { ok: false, error: 'Invalid email or password.' };
  }
  localStorage.setItem(TA_SESSION_KEY, key);
  return { ok: true, user };
}

function taGetCurrentUser() {
  const key = localStorage.getItem(TA_SESSION_KEY);
  if (!key) return null;
  const users = taGetUsers();
  return users[key] || null;
}

function taUpdateProfile(email, profileData) {
  const users = taGetUsers();
  const key = email.trim().toLowerCase();
  if (!users[key]) return false;
  users[key].profile = { ...users[key].profile, ...profileData };
  taSaveUsers(users);
  return true;
}

function taLogout() {
  localStorage.removeItem(TA_SESSION_KEY);
}

function taRequireAuth(loginPath) {
  const user = taGetCurrentUser();
  if (!user) {
    window.location.href = loginPath || '../auth/login.html';
    return null;
  }
  return user;
}

function taRoleRedirect(role) {
  if (role === 'employer') return '../employer/dashboard.html';
  if (role === 'recruiter') return '../recruiter/dashboard.html';
  return '../seeker/dashboard.html';
}

function taInitials(name) {
  return (name || '').trim().split(/\s+/).map(w => w[0]).join('').slice(0, 2).toUpperCase() || 'U';
}