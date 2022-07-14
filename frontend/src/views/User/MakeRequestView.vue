<template>
	<div>
		<header-vue :logout="true" />
		<b-row>
			<b-col md="2">
				<sidebar-vue />
			</b-col>
			<b-col md="10">
				<b-card title="Make Update Request" class="mt-2">
					<user-profile-vue :isAdmin="false" :edit="true" />
				</b-card>
			</b-col>
		</b-row>
	</div>
</template>
<script>
import HeaderVue from '@/components/header/Header.vue';
import SidebarVue from '@/components/sidebar/Sidebar.vue';
import UserProfileVue from '@/components/profile/UserProfile.vue';
export default {
	name: 'MakeRequestView',
	components: { HeaderVue, SidebarVue, UserProfileVue },
};
</script>
