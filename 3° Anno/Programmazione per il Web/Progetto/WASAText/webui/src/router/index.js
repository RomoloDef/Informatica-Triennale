import {createRouter, createWebHashHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SettingsView from '../views/SettingsView.vue';
import ChatView from '../views/ChatView.vue';

const router = createRouter({
	history: createWebHashHistory(import.meta.env.BASE_URL),
	routes: [
		{path: '/', name: 'Home', component: HomeView},
		{path: '/link1', name: 'Link1', component: HomeView},
		{path: '/link2', name: 'Link2', component: HomeView},
		{path: '/some/:id/link', name: 'SomeLink', component: HomeView},
		{path: '/login', name: 'Login', component: LoginView, meta: { hideNavbar: true }},
    {path: '/settings', name: 'Settings', component: SettingsView},
    {path: '/chat/:id', name: 'Chat', component: ChatView }
	]
})

// Navigation Guard 
router.beforeEach((to, from, next) => {
  // Controlla se c'è un ID salvato nel browser
  const isAuthenticated = localStorage.getItem('userId');

  if (to.name !== 'Login' && !isAuthenticated) {
    // Se non vai al login e non sei autenticato -> Vai al Login
    next({ name: 'Login' });
  } else {
    // Altrimenti procedi pure
    next();
  }
});

export default router
