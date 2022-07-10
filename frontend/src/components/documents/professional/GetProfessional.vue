<template>
	<div>
		<b-row>
			<div v-if="isLoading" class="d-flex justify-content-center mb-3">
				<b-spinner
					type="grow"
					variant="info"
					style="width: 3rem; height: 3rem"
					label="loading"
				/>
			</div>
			<template v-else>
				<b-col sm="3">
					<label for="name">Name</label>
				</b-col>
				<b-col sm="9">
					<p>{{ data.name }}</p>
				</b-col>

				<b-col sm="3">
					<label for="name">Year of Achievement</label>
				</b-col>
				<b-col sm="9">
					<p>{{ data.year_of_achievement }}</p>
				</b-col>

				<b-col sm="3">
					<label for="name">Certification</label>
				</b-col>
				<b-col sm="9">
					<a :href="data.document.path" target="blank">View Certification</a>
				</b-col>
			</template>
		</b-row>
	</div>
</template>
<script>
export default {
	name: 'GetProfessionalDocument',
	props: ['user'],
	data() {
		return {
			data: {},
			isLoading: true,
		};
	},
	created() {
		this.getDocument();
	},
	methods: {
		async getDocument() {
			const user = JSON.parse(localStorage.getItem('user'));
			await this.axios
				.get(`api/professional-document/${user.id}/`)
				.then(({ data }) => {
					this.data = data;
					this.isLoading = false;
				})
				.catch(() => {});
		},
	},
};
</script>
<style scoped>
a {
	text-decoration: none;
}
</style>
