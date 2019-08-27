const promessa = async () => {
  try {
    const resposta = await axios.get(
      "https://api.github.com/users/LucasFDutra"
    );
    console.log(resposta);
  } catch (error) {
    console.log(error);
  }
};

promessa();
