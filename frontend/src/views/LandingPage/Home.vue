<template>
	<div class="">
		<header-vue />
		<div
			class="row justify-content-center align-items-center main mx-auto mt-5"
		>
			<div class="col-md-4" role="button" @click="handleClick('user_profile')">
				<div class="card">
					<div class="d-flex flex-column align-items-center w-100 p-5">
						<b-icon icon="person-fill"></b-icon>
						<span style="font-weight: bold; width: fit-content">User</span>
						<span class="text-secondary"> User Dashboard </span>
					</div>
				</div>
			</div>

			<div class="col-md-4" role="button" @click="handleClick('enrolment')">
				<div class="card">
					<div class="d-flex flex-column align-items-center w-100 p-5">
						<b-icon icon="person-plus-fill" aria-hidden="true"></b-icon>
						<span style="font-weight: bold; width: fit-content">Admin</span>
						<span class="text-secondary">Admin Dashboard</span>
					</div>
				</div>
			</div>

			<div
				class="col-md-4"
				role="button"
				@click="handleClick('patner_checkin')"
			>
				<div class="card">
					<div class="d-flex flex-column align-items-center w-100 p-5">
						<b-icon icon="search" aria-hidden="true"></b-icon>
						<span style="font-weight: bold; width: fit-content">Check In</span>
						<span class="text-secondary">Check the Validity of a NIN</span>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import HeaderVue from '../../components/header/Header.vue';
export default {
	name: 'HomeView',
	components: {
		HeaderVue,
	},
	data() {
		return {
			text: 'this is it',
		};
	},
	methods: {
		handleClick(route) {
			if (route != 'patner_checkin') {
				return this.$store.state.isAuthenticated
					? this.$router.push({ name: route })
					: this.$router.push('/login');
			}
			this.$router.push({ name: route });
		},
	},
};
</script>
