<template>
	<div class="">
		<header-vue :logout="true" />
		<b-row class="mt-2">
			<b-col md="2">
				<sidebar-vue />
			</b-col>
			<b-col md="10">
				<b-card :title="title" class="">
					<user-profile :isAdmin="isAdmin" />
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
			isAdmin: false,
			title: '',
			data: {},
			isLoading: true,
		};
	},
	beforeCreate() {},
	created() {},
	mounted() {
		if (!localStorage.getItem('token')) {
			this.$router.push('/login');
		}
		this.isAdmin = this.$route.name === 'enrolment' ? true : false;

		this.title = this.isAdmin ? 'Enrol a User' : 'User Profile';
	},
	methods: {},
};
</script>
