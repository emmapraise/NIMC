<template>
	<div>
		<b-row v-for="(item, index) in education" :key="index">
			<b-col sm="3">
				<label for="highest-education"> {{ item.name }}</label>
			</b-col>
			<b-col sm="9">
				<template v-if="item.type === 'file'">
					<a :href="item.value.path" target="blank"> View {{ item.name }}</a>
				</template>
				<template v-else>
					<p>{{ item.value }}</p>
				</template>
			</b-col>
		</b-row>
	</div>
</template>
<script>
export default {
	name: 'GetEducation',
	props: ['user'],
	data() {
		return {
			data: {},
			education: [
				{
					name: 'Highest Education',
					label: 'highest_education',
					value: '',
				},
				{
					name: 'Year of Graduation',
					label: 'year_of_graduation',
					value: '',
				},
				{
					name: 'Class of Graduation',
					label: 'class_of_graduation',
					value: '',
				},
				{
					name: 'Name of School',
					label: 'name_of_school',
					value: '',
				},
				{
					name: 'Country of Graduation',
					label: 'country_of_graduation',
					value: '',
				},
				{
					name: 'Certificate',
					label: 'certificate',
					type: 'file',
					value: null,
				},
				{
					name: 'Transcript',
					label: 'transcript',
					type: 'file',
					value: null,
				},
			],
		};
	},
	created() {
		this.getDocument();
	},
	methods: {
		async getDocument() {
			await this.axios
				.get(`api/education-document/${this.user.id}/`)
				.then(({ data }) => {
					this.education = this.education.map((obj) => {
						Object.keys(data).map((itemData) => {
							if (obj['label'] === itemData) {
								obj['value'] = data[itemData];
								return obj;
							}
						});
					});
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
