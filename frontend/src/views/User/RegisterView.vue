<template>
	<div class="container">
		<user-profile />
	</div>
</template>
<script>
import UserProfile from '../../components/profile/UserProfile.vue';
export default {
	name: 'RegisterView',
	components: {
		UserProfile,
	},
	data() {
		return {};
	},
	mounted() {
		console.log('object');
	},
	methods: {
		// done() {
		// 	console.log(this.personal_data_tab);
		// },
	},
};
</script>
