<template>
	<div>
		<b-row>
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
				})
				.catch((err) => {
					console.log(err);
				});
		},
	},
};
</script>
