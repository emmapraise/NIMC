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
				<b-col sm="3">CV</b-col>
				<b-col sm="9"
					><a :href="data.cv.path" target="blank"> View CV</a></b-col
				>
			</template>
		</b-row>
	</div>
</template>
<script>
export default {
	name: 'GetCVComponent',
	props: ['user'],
	data() {
		return {
			isLoading: true,
			data: {},
		};
	},
	created() {
		this.getDocument();
	},
	methods: {
		async getDocument() {
			await this.axios
				.get(`api/cv/${this.user.id}/`)
				.then(({ data }) => {
					console.log(data);
					this.data = data;
					this.isLoading = false;
				})
				.catch((err) => {
					console.error(err);
				});
		},
	},
};
</script>
<style scoped>
a {
	text-decoration: none;
}
</style>
