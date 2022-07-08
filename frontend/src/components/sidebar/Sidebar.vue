<template>
	<div class="justify-content-center align-items-center">
		<div class="mt-2 justify-content-center align-items-center text-center">
			<b-avatar :src="Avatar" size="7rem" class=""></b-avatar>
			<div>
				<p class="text-center font-weight-bold m-0 p-0 mt-2">
					{{ user.first_name }} {{ user.last_name }}
				</p>
				<p class="text-center m-0 p-0 font-weight-light">NIN: {{ user.nin }}</p>
			</div>
		</div>
		<b-nav
			vertical
			class="mt-2 justify-content-center align-items-center"
			v-for="(item, index) in sidebar_menu"
			:key="index"
		>
			<router-link
				:to="{ name: `${item.label}` }"
				style="text-decoration: none"
				>{{ item.name }}</router-link
			>
		</b-nav>
	</div>
</template>
<script>
import Avatar from '../../assets/images/avatar.webp';
export default {
	name: 'SidebarComponent',
	mounted() {
		this.getUsers();
	},
	data() {
		return {
			Avatar,
			user: {},
			sidebar_menu: [],
			admin_sidebar: [
				{
					name: 'Enroll A User',
					label: 'enrolment',
					path: '/admin',
				},
				{
					name: 'Upload Document',
					label: 'upload_document',
					path: '/admin/upload',
				},
				{
					name: 'Update Requests',
					label: 'update_request',
					path: '/admin/request',
				},
			],
			user_sidebar: [
				{
					name: 'Enroll A User',
					label: 'user_profile',
					path: '/user/profile',
				},
				{
					name: 'Documents',
					label: 'documents',
					path: '/user/documents',
				},
				{
					name: 'Update Request',
					label: 'make-request',
					path: '/user/make-request',
				},
			],
		};
	},
	methods: {
		getUsers() {
			const userData = localStorage.getItem('user');
			this.user = JSON.parse(userData);
			this.sidebar_menu = this.user.is_admin
				? this.admin_sidebar
				: this.user_sidebar;
		},
	},
};
</script>
