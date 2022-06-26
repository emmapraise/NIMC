<template>
	<div>
		<b-navbar toggleable="lg" type="dark" variant="info">
			<b-navbar-brand href="/" tag="h1">NIMC</b-navbar-brand>

			<b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

			<b-collapse id="nav-collapse" is-nav>
				<!-- <b-navbar-nav>
					<b-nav-item href="#">Link</b-nav-item>
					<b-nav-item href="#" disabled>Disabled</b-nav-item>
				</b-navbar-nav> -->

				<!-- Right aligned nav items -->
				<b-navbar-nav class="ml-auto">
					<!-- <b-nav-form>
						<b-form-input
							size="sm"
							class="mr-sm-2"
							placeholder="Search"
						></b-form-input>
						<b-button size="sm" class="my-2 my-sm-0" type="submit"
							>Search</b-button
						>
					</b-nav-form> -->
					<div v-show="logout">
						<b-button variant="danger" @click.prevent="logoutAction"
							>Logout</b-button
						>
					</div>
				</b-navbar-nav>
			</b-collapse>
		</b-navbar>
	</div>
</template>
<script>
export default {
	name: 'HeaderComponent',
	props: ['logout'],
	data() {
		return {};
	},
	methods: {
		logoutAction() {
			console.log('first');
			this.axios
				.post(`api/logout/`)
				.then((result) => {
					console.log(result);
					localStorage.removeItem('token');
					localStorage.removeItem('user');
					this.$store.commit('removeToken');
					this.$router.push({ name: 'home' });
				})
				.catch((err) => {
					console.log(err);
				});
		},
	},
};
</script>
