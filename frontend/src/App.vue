<template>
	<div id="app">
		<nav>
			<!-- <router-link to="/">Home</router-link> |
			<router-link to="/about">About</router-link> -->
		</nav>
		<router-view />
	</div>
</template>
<script>
import store from './store';

export default {
	name: 'AppComponent',
	beforeCreate() {
		this.$store.commit(store.initalizeStore);

		const token = this.$store.state.token;
		if (token) {
			this.axios.defaults.headers.common['Authorization'] = 'Token ' + token;
		} else {
			this.axios.defaults.headers.common['Authorization'] = '';
		}
	},
};
</script>
<style lang="scss"></style>
