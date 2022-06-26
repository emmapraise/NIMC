<template>
	<div id="app">
		<router-view />
	</div>
</template>
<script>
export default {
	name: 'AppComponent',
	beforeCreate() {
		this.$store.commit('initalizeStore');

		const token = this.$store.state.token;
		if (token) {
			this.axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
		} else {
			this.axios.defaults.headers.common['Authorization'] = '';
		}
	},
};
</script>
<style lang="scss"></style>
