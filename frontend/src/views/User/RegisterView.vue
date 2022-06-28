<template>
	<div class="">
		<header-vue :logout="true" />
		<b-row class="mt-2">
			<b-col md="2">
				<sidebar-vue />
			</b-col>
			<b-col md="10">
				<b-card :title="title" class="">
					<!-- <b-form
						@submit.prevent="onSubmit"
						validated="true"
						class="was-validated"
					> -->
					<user-profile :ninInfoData="data" />
					<!-- </b-form> -->
				</b-card>
			</b-col>
		</b-row>
	</div>
</template>
<script>
import HeaderVue from '../../components/header/Header.vue';
import SidebarVue from '../../components/sidebar/Sidebar.vue';
import UserProfile from '../../components/profile/UserProfile.vue';
export default {
	name: 'RegisterView',
	components: {
		UserProfile,
		HeaderVue,
		SidebarVue,
	},
	data() {
		return {
			is_admin: false,
			title: '',
			data: {},
		};
	},
	beforeCreate() {
		if (!localStorage.getItem('token')) {
			this.$router.push('/login');
		}
		this.is_admin = this.$route.name === 'enrolment' ? true : false;
	},
	mounted() {
		this.getUserProfile();
		this.title = this.is_admin ? 'Enrol a User' : 'User Profile';
	},
	methods: {
		getUserProfile() {
			const user = JSON.parse(this.$store.state.user);
			this.axios
				.get(`api/nininfo/${user.id}/`)
				.then((result) => {
					console.log(result);
					this.data = result;
				})
				.catch((err) => {
					console.log(err);
				});
		},
	},
};
</script>
