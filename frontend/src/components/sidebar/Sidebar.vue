<template>
	<div class="justify-content-center align-items-center">
		<div class="mt-2">
			<b-img
				center
				src="https://picsum.photos/125/125/?image=58"
				alt="Center image"
				rounded="circle"
			></b-img>
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
export default {
	name: 'SidebarComponent',
	data() {
		return {
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
