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
					<label for="certificate"> Certificate</label>
				</b-col>
				<b-col sm="9">
					<a :href="data.certificate.path" target="blank"> View Certificate</a>
				</b-col>

				<b-col sm="3">
					<label for="transcript"> Transcript</label>
				</b-col>
				<b-col sm="9">
					<a :href="data.transcript.path" target="blank"> View Transcript</a>
				</b-col>
			</template>
		</b-row>
	</div>
</template>
<script>
export default {
	name: 'GetCertificate',
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
			await this.axios
				.get(`api/certificate/${this.user.id}/`)
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
