<template>
	<div class="">
		<header-vue />
		<b-row class="mt-2">
			<b-col md="2">
				<sidebar-vue />
			</b-col>
			<b-col md="10">
				<b-card title="Enrol A User" class="">
					<b-form validated="true" class="was-validated">
						<user-profile /> <br />

						<div class="mt-5 float-right" align-h="end">
							<b-button size="lg" variant="success" type="submit"
								>Submit</b-button
							>
						</div>
					</b-form>
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
		return {};
	},
	mounted() {
		// console.log('object');
	},
	methods: {
		onsubmit() {
			console.log('object');
		},
	},
};
</script>
