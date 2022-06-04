<template>
	<div class="container mt-3">
		<b-card title="Enrol A User">
			<b-form @submit.prevent="onSubmit" validated="true" class="was-validated">
				<user-profile />
				<div class="mt-5 float-right" align-h="end">
					<b-button size="lg" variant="success">Submit</b-button>
				</div>
			</b-form>
		</b-card>
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
		onsubmit() {
			console.log('object');
		},
	},
};
</script>
