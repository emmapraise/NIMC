<template>
	<div class="justify-content-center align-items-center">
		<div class="mt-2 justify-content-center align-items-center text-center">
			<b-avatar :src="Avatar" size="7rem" class=""></b-avatar>
			<div>
				<p class="text-center font-weight-bold m-0 p-0 mt-2">
					Oludare Emmanuel
				</p>
				<p class="text-center m-0 p-0 font-weight-light">NIN: 4636363</p>
			</div>
		</div>
		<b-nav
			vertical
			class="mt-2 justify-content-center align-items-center"
			v-for="(item, index) in sidebar_link"
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
import Avatar from '../../assets/images/download.jpeg';
export default {
	name: 'SidebarComponent',
	data() {
		return {
			Avatar,
			sidebar_link: [
				{
					name: 'Profile',
					label: 'profile',
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
		};
	},
};
</script>
